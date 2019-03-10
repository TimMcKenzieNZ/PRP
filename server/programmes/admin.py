from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .forms import UpdateForm, DeliverableForm
from .models import *

# Do we want to actually define an admin group or just user the superuser boolean?
def request_user_is_admin(request):
    """Checks if the request user belongs to the administrator group"""
    return request.user.groups.values_list('name').filter(name='administrator').exists()


class ProjectAdmin(ModelAdmin):

    """Fields to show in the form"""
    def get_fieldsets(self, request, obj=None):
        return (
            ('Details', {
                'fields': ('name', 'description', 'priority', 'start_date', 'end_date', 'cost', 'image')
            }),
            ('Status', {
                'fields': ('progress', 'status')
            }),
            ('Relationships', {
                'fields': ('goals',)
            }),
        )


class InitiativeAdmin(ModelAdmin):
    """Fields to show in the form"""
    def get_fieldsets(self, request, obj=None):
        if request_user_is_admin(request):
            return (
                ('Details', {
                    'fields': ('name', 'description', 'start_date', 'end_date')
                }),
                ('Status', {
                    'fields': ('progress', 'status')
                }),
                ('Relationships', {
                    'fields': ('risks', 'outputs', 'projects')
                }),
                (None, {
                    'fields': ('order', 'adapter_id', 'adapter_ref')
                }),

            )
        return ( # Hidden fields: order, adapter_id, adapter_ref, outputs
                ('Details', {
                    'fields': ('name', 'description', 'start_date', 'end_date')
                }),
                ('Status', {
                    'fields': ('progress', 'status')
                }),
                ('Relationships', {
                    'fields': ('risks', 'projects')
                }),

        )


class RiskAdmin(ModelAdmin):
    """Fields to show in the form"""
    def get_fieldsets(self, request, obj=None):
        if request_user_is_admin(request):

            return (
                (None, { # Can arrange returned data using headers
                    'fields': (
                        'name',
                        'description',
                        'likelihood',
                        'impact',
                        'flagged',
                        'mitigations',
                        'risk_category',
                        'initiatives'
                    )
                }),
            )
        return (
            (None, { 
                'fields': (
                    'name',
                    'description',
                    'likelihood',
                    'impact',
                    'flagged',
                    'mitigations',
                    'initiatives'
                )
            }),
        )

class UpdateAdmin(ModelAdmin):
    form = UpdateForm

class TeamMemberAdmin(ModelAdmin):
    """Fields to show in the form"""
    def get_fieldsets(self, request, obj=None):
        if request_user_is_admin(request):
            return (
                ('Personal Info', {
                    'fields': ('username', 'email', 'first_name', 'last_name', 'position', 'image', 'contact_number')
                }),
                ('Status', {
                    'fields': ('is_active', 'is_staff')
                }),
                ('Permissions', {
                    'fields': ('groups', 'user_permissions')
                }),
                (None, {
                    'fields': ('last_login', 'date_joined')
                })

            )
        return (
            ('Personal Info', {
                'fields': ('username', 'email', 'first_name', 'last_name', 'position', 'contact_number')
            }),

        )


"""Links the Deliverable form class to the django admin website"""
class DeliverableAdmin(ModelAdmin):

    form = DeliverableForm

    """Overwriting the Django admin Deliverable save function to include the name of the project manager who updated it"""
    def save_model(self, request, obj, form, change):
        if (change):
            obj.author = request.user
            old_deliverable = Deliverable.objects.filter(id=obj.id)[0]
            template = "{} changed from {} to {}. "
            log = ""
            if old_deliverable.team_impact != obj.team_impact:
                log += template.format("Team impact", old_deliverable.team_impact, obj.team_impact)
            if old_deliverable.sponsor_impact != obj.sponsor_impact:
                log += template.format("Sponsor impact", old_deliverable.sponsor_impact, obj.sponsor_impact)
            if old_deliverable.pm_impact != obj.pm_impact:
                log += template.format("PM impact", old_deliverable.pm_impact, obj.pm_impact)
            if log == "":
                log = "No impact change."
            obj.log = log
        super().save_model(request, obj, form, change)
    
    """Fields to show in the form"""
    def get_fieldsets(self, request, obj=None):
        if request_user_is_admin(request):
            return (
                ('Details', {
                    'fields': ('name', 'description', 'end_date', 'initiative', 'order')
                }),
                ('Status', {
                    'fields': ('progress','status', 'status_message', 'team_impact', 'sponsor_impact', 'pm_impact')
                }),
            )
         # We hide the status update fields if the deliverable is being created for the first time
        if request.path == '/admin/programmes/deliverable/add/': # Is there a better option than hardcoding the path?
            return (
                (None, {
                    'fields': ('name', 'description', 'end_date', 'initiative', 'status')
                }),
            )
        return (
            ('Details', {
                'fields': ('name', 'description', 'end_date', 'initiative')
            }),
            ('Status Update', {
                'fields': ('progress','status', 'status_message', 'team_impact', 'sponsor_impact', 'pm_impact')
            }),
        )


class ProgrammeAdmin(ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # when you create a programme's name it automatically updates the slug

class GoalAdmin(ModelAdmin):

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "category":
    #         kwargs["queryset"] = Category.objects.filter(name__in=['God', 'Demi God'])
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    """Fields to show in the form"""
    def get_fieldsets(self, request, obj=None):
        programme = request.user.id
        print(programme)
        if request_user_is_admin(request):
            return (
                (None, {
                    'fields': ('name', 'description', 'image', 'order', 'programme', 'problems')
                }),

            )
        return (
            (None, {
                'fields': ('name', 'description', 'image', 'programme', 'problems')
            }),

        )

# Registering different modeladmins gives those modeladmin attributes to the model's page (.e.g delete permissions)
admin.site.register(Problem)
admin.site.register(Goal, GoalAdmin)
admin.site.register(Initiative, InitiativeAdmin)
admin.site.register(Programme, ProgrammeAdmin)
admin.site.register(Target)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Benefit)
admin.site.register(Deliverable, DeliverableAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(RiskMitigationStrategy)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Update)
admin.site.register(Role)



# Currently we do not need to serve up any of these models to a Project Manager:
# admin.site.register(Stakeholder)
# admin.site.register(Team)
# admin.site.register(Milestone)
# admin.site.register(MilestoneHistory)
# admin.site.register(MilestoneStatus)
# admin.site.register(RiskCategory)
# admin.site.register(Role)
# admin.site.register(Outcome)
