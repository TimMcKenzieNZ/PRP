from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
import itertools

class Command(BaseCommand):
  """
  Command to set permissions & groups for the prp database
  """


  help = 'Add the PRP roles & permissions'

  def handle(self, *args, **options):
    
    # Get the active database
    database = options.get('database', 'default')

    # We need the contenttype if we are going to add custom permissions
    content_type, created = ContentType.objects.using(database).get_or_create(app_label='global', model='global')

    # function to create custom permission
    def permission(codename, name):
      return Permission.objects.using(database).get_or_create(codename=codename, name=name, content_type=content_type)[0]
    
    # example custom permission:
    # view_all_foobars = permission('view_all_foobars', 'View all foobars')

    # registering all the default CRUD action permissions for the models in the db
    view_initiative = Permission.objects.using(database).get(codename='view_initiative')
    add_initiative = Permission.objects.using(database).get(codename='add_initiative')
    change_initiative = Permission.objects.using(database).get(codename='change_initiative')
    delete_initiative = Permission.objects.using(database).get(codename='delete_initiative')

    view_deliverable = Permission.objects.using(database).get(codename='view_deliverable')
    add_deliverable = Permission.objects.using(database).get(codename='add_deliverable')
    change_deliverable = Permission.objects.using(database).get(codename='change_deliverable')
    delete_deliverable = Permission.objects.using(database).get(codename='delete_deliverable')

    view_benefit = Permission.objects.using(database).get(codename='view_benefit')
    add_benefit = Permission.objects.using(database).get(codename='add_benefit')
    change_benefit = Permission.objects.using(database).get(codename='change_benefit')
    delete_benefit = Permission.objects.using(database).get(codename='delete_benefit')

    view_goal = Permission.objects.using(database).get(codename='view_goal')
    add_goal = Permission.objects.using(database).get(codename='add_goal')
    change_goal = Permission.objects.using(database).get(codename='change_goal')
    delete_goal = Permission.objects.using(database).get(codename='delete_goal')

    view_risk = Permission.objects.using(database).get(codename='view_risk')
    add_risk = Permission.objects.using(database).get(codename='add_risk')
    change_risk = Permission.objects.using(database).get(codename='change_risk')
    delete_risk = Permission.objects.using(database).get(codename='delete_risk')

    view_problem = Permission.objects.using(database).get(codename='view_problem')
    add_problem = Permission.objects.using(database).get(codename='add_problem')
    change_problem = Permission.objects.using(database).get(codename='change_problem')
    delete_problem = Permission.objects.using(database).get(codename='delete_problem')

    view_project = Permission.objects.using(database).get(codename='view_project')
    add_project = Permission.objects.using(database).get(codename='add_project')
    change_project = Permission.objects.using(database).get(codename='change_project')
    delete_project = Permission.objects.using(database).get(codename='delete_project')

    view_outcome = Permission.objects.using(database).get(codename='view_outcome')
    add_outcome = Permission.objects.using(database).get(codename='add_outcome')
    change_outcome = Permission.objects.using(database).get(codename='change_outcome')
    delete_outcome = Permission.objects.using(database).get(codename='delete_outcome')

    view_programme = Permission.objects.using(database).get(codename='view_programme')
    add_programme = Permission.objects.using(database).get(codename='add_programme')
    change_programme = Permission.objects.using(database).get(codename='change_programme')
    delete_programme = Permission.objects.using(database).get(codename='delete_programme')

    view_riskmitigationstrategy = Permission.objects.using(database).get(codename='view_riskmitigationstrategy')
    add_riskmitigationstrategy = Permission.objects.using(database).get(codename='add_riskmitigationstrategy')
    change_riskmitigationstrategy = Permission.objects.using(database).get(codename='change_riskmitigationstrategy')
    delete_riskmitigationstrategy = Permission.objects.using(database).get(codename='delete_riskmitigationstrategy')

    view_role = Permission.objects.using(database).get(codename='view_role')
    add_role = Permission.objects.using(database).get(codename='add_role')
    change_role = Permission.objects.using(database).get(codename='change_role')
    delete_role = Permission.objects.using(database).get(codename='delete_role')

    view_teammember = Permission.objects.using(database).get(codename='view_teammember')
    add_teammember = Permission.objects.using(database).get(codename='add_teammember')
    change_teammember = Permission.objects.using(database).get(codename='change_teammember')
    delete_teammember = Permission.objects.using(database).get(codename='delete_teammember')

    view_group = Permission.objects.using(database).get(codename='view_group')
    add_group = Permission.objects.using(database).get(codename='add_group')
    change_group = Permission.objects.using(database).get(codename='change_group')
    delete_group = Permission.objects.using(database).get(codename='delete_group')

    view_permission = Permission.objects.using(database).get(codename='view_permission')
    add_permission = Permission.objects.using(database).get(codename='add_permission')
    change_permission = Permission.objects.using(database).get(codename='change_permission')
    delete_permission = Permission.objects.using(database).get(codename='delete_permission')

    view_update = Permission.objects.using(database).get(codename='view_update')
    add_update = Permission.objects.using(database).get(codename='add_update')
    change_update = Permission.objects.using(database).get(codename='change_update')
    delete_update = Permission.objects.using(database).get(codename='delete_update')

    view_memberrole = Permission.objects.using(database).get(codename='view_role')
    add_memberrole = Permission.objects.using(database).get(codename='add_role')
    change_memberrole = Permission.objects.using(database).get(codename='change_role')
    delete_memberrole = Permission.objects.using(database).get(codename='delete_role')

    # Define the groups and what permissions each group will have
    groups = [
      {
        'name': 'administrator',
        'description': 'In charge of managing the server & database. They have full permissions',
        'permissions': [view_initiative,
                        add_initiative,
                        change_initiative,
                        delete_initiative,

                        view_benefit,
                        add_benefit,
                        change_benefit,
                        delete_benefit,

                        view_goal,
                        add_goal,
                        change_goal,
                        delete_goal,

                        view_deliverable,
                        add_deliverable,
                        change_deliverable,
                        delete_deliverable,

                        view_project,
                        add_project,
                        change_project,
                        delete_project,

                        view_risk,
                        add_risk,
                        change_risk,
                        delete_risk,

                        view_outcome,
                        add_outcome,
                        change_outcome,
                        delete_outcome,

                        view_problem,
                        add_problem,
                        change_problem,
                        delete_problem,

                        view_programme,
                        add_programme,
                        change_programme,
                        delete_programme,

                        view_riskmitigationstrategy,
                        add_riskmitigationstrategy,
                        change_riskmitigationstrategy,
                        delete_riskmitigationstrategy,

                        view_role,
                        add_role,
                        change_role,
                        delete_role,

                        view_teammember,
                        add_teammember,
                        change_teammember,
                        delete_teammember,

                        view_group,
                        add_group,
                        change_group,
                        delete_group,

                        view_permission,
                        add_permission,
                        change_permission,
                        delete_permission,

                        view_update,
                        add_update,
                        change_update,
                        delete_update,

                        view_memberrole,
                        add_memberrole,
                        change_memberrole,
                        delete_memberrole,

                        
                        ]
      },
      {
        'name': 'director',
        'description': 'In charge of a programme, represents upper management',
        'permissions': [

                        view_benefit,
                        add_benefit,
                        change_benefit,
                        delete_benefit,

                        view_goal,
                        add_goal,
                        change_goal,
                        delete_goal,

                        view_problem,
                        add_problem,
                        change_problem,
                        delete_problem,

                        view_programme,
                        add_programme,
                        change_programme,
                        delete_programme,

                        view_teammember,
                        
                        ]
      },
      {
        'name': 'project_manager',
        'description': 'Individual in charge of a programme\'s projects',
        'permissions': [view_initiative,
                        add_initiative,
                        change_initiative,
                        delete_initiative,

                        view_deliverable,
                        add_deliverable,
                        change_deliverable,
                        delete_deliverable,

                        view_project,
                        add_project,
                        change_project,
                        delete_project,

                        view_risk,
                        add_risk,
                        change_risk,
                        delete_risk,

                        view_outcome,
                        add_outcome,
                        change_outcome,
                        delete_outcome,

                        view_riskmitigationstrategy,
                        add_riskmitigationstrategy,
                        change_riskmitigationstrategy,
                        delete_riskmitigationstrategy,

                        view_role,
                        add_role,
                        change_role,
                        delete_role,

                        view_update,

                        view_teammember,
                        
                        view_benefit,

                        view_memberrole,
                        add_memberrole,
                        change_memberrole,
                        delete_memberrole,
                        ]
      },
      {
        'name': 'team_member',
        'description': 'any member of a project or programme that is not in a leadership position',
        'permissions': [view_initiative,

                        view_deliverable,
                        add_deliverable,
                        change_deliverable,

                        view_update,

                        ]
      }
    ]

    # gets the permissions for the given group
    def _get_permissions(group_name):
      group = [g for g in groups if g['name'] == group_name][0]

      return group['permissions']

    # for each group in our group dictionary, we create the group and set their permissions
    for group in groups:
      group_db_object = Group.objects.using(database).get_or_create(name=group['name'])[0]
      group_db_object.permissions.set(_get_permissions(group['name']))
      self.stdout.write(self.style.SUCCESS('Created group and permissions for group {}'.format(group['name'])))
