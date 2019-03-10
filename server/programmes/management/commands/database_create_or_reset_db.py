from django.core.management.base import BaseCommand
from django.core.management import call_command
from programmes.utils import run_script, run_sql, user_exists, safety_check_is_production
from django.conf import settings
import os

# Command wholeheartedly lifted from Ewen's work in resource consents

class Command(BaseCommand):
    help = 'Initialise the public schema (WARNING: will destroy anything in the public schema)'

    def handle(self, *args, **options):
        database = options.get('database', 'default')

        # Run a safety check
        if safety_check_is_production(database=database):
            raise EnvironmentError('ATTEMPTING TO RUN IN PRODUCTION - ABORTING')

        # Reset Schema
        run_sql('DROP SCHEMA IF EXISTS public CASCADE; CREATE SCHEMA public; ')
        
        # create superuser
        # run_sql('CREATE USER {} WITH PASSWORD "password";'
        #         .format(settings.DATABASES[database]['USER'], database=database))

        # # give privileges to superuser

        # run_sql('GRANT ALL PRIVILEGES ON DATABASE {} TO {};'
        #         .format(settings.DATABASES[database]['NAME'], settings.DATABASES[database]['USER'], database=database))

        
