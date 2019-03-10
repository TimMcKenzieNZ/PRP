from programmes.models import Update
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
import os
from django.conf import settings
from subprocess import check_output, STDOUT, CalledProcessError
from shlex import quote
from django.db import connections, connection
from psycopg2.extensions import quote_ident


def run_script(path, database='default', pg_options=None):
    if not os.path.exists(path):
        raise ValueError('SQL file does not exist "{}"'.format(path))
    psql_command = _get_psql_command(database, pg_options)
    cmd = '{} < {}'.format(psql_command, path)
    out = check_output(cmd, stderr=STDOUT, shell=True)
    _raise_if_error_in_output(out, cmd)


def user_exists(username, database='default'):
    """"Check if a user exists in the database"""
    with connections[database].cursor() as cursor:
        cursor.execute('SELECT 1 FROM pg_roles WHERE rolname=%s', (username,))
        return bool(cursor.fetchall())
        

def _get_psql_command(database, pg_options):
    if database not in settings.DATABASES:
        raise ValueError('Invalid database given "{}"'.format(database))

    psql_command = 'PGPASSWORD={} psql --host="{}" --dbname={} --port="{}" --user="{}"'.format(
        settings.DATABASES[database]['PASSWORD'] or '',
        settings.DATABASES[database]['HOST'],
        settings.DATABASES[database]['NAME'],
        settings.DATABASES[database]['PORT'],
        settings.DATABASES[database]['USER'])

    # Add PG_OPTIONS to the command if any are set
    if pg_options:
        psql_command = 'PGOPTIONS={} {}'.format(quote(pg_options), psql_command)

    return psql_command


def _raise_if_error_in_output(out, cmd):
    # SQL Errors don't give a failed return code so we'll check the output and raise
    # an exception if there are any "ERROR:" lines in there.
    # NOTE: Temporary disabling 'must be owner of database' and 'permission denied
    # to set parameter' errors as we get them in AWS. Ewen 03/11/17
    lines = out.decode(encoding='UTF-8').split("\n")
    if any(line.startswith('ERROR:')
           for line in lines):
        print(out.decode(encoding='UTF-8'))
        raise CalledProcessError(returncode=0, cmd=cmd, output=out)


def run_sql(sql, database='default', pg_options=None):
    print(sql)
    psql_command = _get_psql_command(database, pg_options)
    cmd = 'echo {} | {}'.format(quote(sql), psql_command)
    out = check_output(cmd, stderr=STDOUT, shell=True)
    _raise_if_error_in_output(out, cmd)


def escape_identifier(identifier, cursor):
    """
    Escape a PostgreSQL identifier e.g. Column, Table.

    Will split apart by '.', so schema and tables are handled.

    Examples:
        application.application -> "application"."application"
        lib_lookup -> "lib_lookup"

    Cursor is needed as psycopg uses that to get the right encoding.
    """
    # Refers to cursor.cursor so as to get at the psycopg cursor rather than
    # the Django wrapper.
    return '.'.join(quote_ident(v, cursor.cursor) for v in identifier.split('.'))


def safety_check_is_production(database='default'):
    """"
    Test if this is a production environment by checking for a setting in the
    environment_setting table.
    """
    schema = 'public'
    table = 'environment_setting'
    setting_key = 'environment'
    setting_value = 'production'

    with connections[database].cursor() as cursor:
        cursor.execute('SELECT 1 FROM information_schema.tables WHERE table_schema=%s AND table_name=%s', (schema, table))
        table_exists = bool(cursor.fetchall())
        if not table_exists:
            return False

        schema_and_table = '{}.{}'.format(schema, table)
        cursor.execute('SELECT 1 FROM ' + escape_identifier(schema_and_table, cursor) +
                       ' WHERE setting_key=%s AND setting_value=%s', (setting_key, setting_value))
        is_production = bool(cursor.fetchall())

    return is_production


"""
Creates a log string based on what impacts changed in a deliverable IF it was updated.
"""
def generate_update_log(sender, instance, **kwargs):
    try:
        update = Update(author=instance.author, 
                        date=datetime.datetime.today().date(), 
                        log=instance.log,
                        deliverable=instance,
                        description=instance.status_message)
        update.save()
    except AttributeError as error:
        # The deliverable is being created for the first time
        pass
