from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from programmes.modelAttributeValidators import *
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
import datetime








# Various types of status
OVERDUE = 'Overdue'
COMPLETE = 'Complete'
IN_PROGRESS = 'In Progress'
NOT_STARTED = 'Not Started'
BLOCKED = 'Blocked'
DEFERRED = 'Deferred'
CANCELLED = 'Cancelled'
DELAYED = 'Delayed'

STATUS_CHOICES = (
    (OVERDUE, 'Overdue'),
    (COMPLETE, 'Complete'),
    (IN_PROGRESS, 'In Progress'),
    (NOT_STARTED, 'Not Started'),
    (BLOCKED, 'Blocked'),
    (DEFERRED, 'Deferred'),
    (CANCELLED, 'Cancelled'),
    (DELAYED, 'Delayed'),
)

# Priority choices
MINOR = 'minor'
LOW = 'low'
MEDIUM = 'medium'
HIGH = 'high'
CRITICAL = 'critical'
UNKNOWN = 'unknown'

PRIORITY_CHOICES = (
    (UNKNOWN, 'Unknown'),
    (MINOR, 'Minor'),
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
    (HIGH, 'High'),
    (CRITICAL, 'Critical')
)

# Severity choices
NO_IMPACT = 'none'
LOW_IMPACT = 'low'
MODERATE_IMPACT = 'moderate'
SEVERE_IMPACT = 'severe'

IMPACT_CHOICES = (
    (NO_IMPACT, 'None'),
    (LOW_IMPACT, 'Low'),
    (MODERATE_IMPACT, 'Moderate'),
    (SEVERE_IMPACT, 'Severe')
)

# Risk choices
R_VERY_LOW = 1
R_LOW = 2
R_MODERATE = 3
R_HIGH = 4
R_VERY_HIGH = 5

RISK_CHOICES = (
    (R_VERY_LOW, 'Very Low'),
    (R_LOW, 'Low'),
    (R_MODERATE, 'Moderate'),
    (R_HIGH, 'High'),
    (R_VERY_HIGH, 'Very High')
)

C_MINOR = "Minor"
C_MODERATE = "Moderate"
C_MAJOR = "Major"

RISK_CATEGORY_CHOICES = (
    (C_MINOR, "Minor"),
    (C_MODERATE, "Moderate"),
    (C_MAJOR, "Major")
)

# Role choices
NO_ROLE = "No Role"
CONSULTANT = "Consultant"
TEAMMEMBER = "Project Team Member"
MANAGER = "Project Manager"
ANALYEST = "Analyst"
CLIENT = "Client"
SPONSOR = "Sponsor"
ADMINISTRATOR = "Administrator"
DEVELOPER = "Developer"
SUPPORT = "Support"
SUPPLIER = "Supplier"
STAKEHOLDER = "Stakeholder"
TESTER = "Tester"
User = "User"
DOMAINEXPERT = "Domain Expert"
QUALITYASSURANCE = "Quality Assurance"
DESIGNER = "Designer"
TECHNICIAN = "Technician"
TEAMLEADER = "Team Leader"

ROLE_CHOICES = (
    (NO_ROLE, "No Role"),
    (CONSULTANT, "Consultant"),
    (TEAMMEMBER, "Project Team Member"),
    (MANAGER , "Project Manager"),
    (ANALYEST , "Analyst"),
    (CLIENT , "Client"),
    (SPONSOR , "Sponsor"),
    (ADMINISTRATOR , "Administrator"),
    (DEVELOPER , "Developer"),
    (SUPPORT , "Support"),
    (SUPPLIER , "Supplier"),
    (STAKEHOLDER , "Stakeholder"),
    (TESTER , "Tester"),
    (User , "User"),
    (DOMAINEXPERT , "Domain Expert"),
    (QUALITYASSURANCE , "Quality Assurance"),
    (DESIGNER , "Designer"),
    (TECHNICIAN , "Technician"),
    (TEAMLEADER , "Team Leader")
)


class TeamMember(AbstractUser):
    #teams = models.ManyToManyField(Team, related_name='team_members')
    email = models.EmailField(blank=False)
    position = models.CharField(max_length=200)
    image = models.ImageField(default=None, upload_to='prp/teammembers/images', blank=True)
    contact_number = models.PositiveIntegerField(default=None, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta():
        db_table = "team_member"

    class JSONAPIMeta:
        resource_name = "teammembers"


User = get_user_model()


class Stakeholder(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    contact_name = models.CharField(blank=False, max_length=200)
    contact_email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "stakeholders"



class Outcome(models.Model):
    name = models.CharField(blank=False, max_length=100)
    pros = models.TextField()
    cons = models.TextField()
    description = models.TextField()
    date = models.DateField(datetime.date.today())

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "outcomes"





class Team(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "teams"


class MilestoneStatus(models.Model):

    status = models.CharField(
        max_length = 12,
        choices = STATUS_CHOICES,
        default=NOT_STARTED,
    )

    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta():
        db_table = "milestone_status"

    class JSONAPIMeta:
        resource_name = "milestone_status's"








class Programme(models.Model):
    name = models.CharField(blank=False, max_length=40, unique=True)
    description = models.TextField()
    vision = models.TextField()
    image = models.ImageField(upload_to='prp/programmes/images')
    start_date = models.DateField(datetime.date.today(), blank=False)
    end_date = models.DateField(blank=False, null=False)
    slug = models.SlugField()
    members = models.ManyToManyField(TeamMember, related_name='programmes')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is None: # Prevents the slug changing if the programme name is changed
            self.slug = slugify(self.name)
        super(Programme, self).save(*args, **kwargs)

    class JSONAPIMeta:
       resource_name = "programmes"



class Problem(models.Model):
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "problems"
 




class Goal(models.Model):
   
    problems = models.ManyToManyField(Problem, related_name='goals')
    programme = models.ForeignKey(Programme, related_name="goals", on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=200)
    image = models.ImageField(upload_to='prp/goals/images')
    description = models.TextField()
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "goals"


class Project(models.Model):

    goals = models.ManyToManyField(Goal, related_name='projects')
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    start_date = models.DateField(datetime.date.today(), blank=False)
    end_date = models.DateField(validators=[validate_date_not_in_past], blank=False, null=False)
    progress = models.FloatField(validators=[validate_progress])
    priority = models.CharField(max_length = 8, choices=PRIORITY_CHOICES, default=R_VERY_LOW)
    cost = models.PositiveIntegerField()
    image = models.ImageField(upload_to='prp/projects/images')
    status = models.CharField(max_length = 12, choices = STATUS_CHOICES, default=NOT_STARTED)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "projects"



class Initiative(models.Model):
    # This is to show the risks table in django admin. When an initiative is created, it should have risks attached to it
    risks = models.ManyToManyField('Risk',
            db_table='app_propertytype_initiatives', blank=True)

    outputs = models.ManyToManyField(Outcome, related_name="initiatives", blank=True)
    projects = models.ManyToManyField(Project, related_name="initiatives")


    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    start_date = models.DateField(datetime.date.today(), blank=False)
    end_date = models.DateField(validators=[validate_date_not_in_past], blank=False)
    progress = models.FloatField(validators=[validate_progress])
    status = models.CharField(
        max_length = 12,
        choices = STATUS_CHOICES,
        default=NOT_STARTED,
    )
    adapter_id = models.PositiveIntegerField(default=1)
    adapter_ref = models.CharField(blank=False, max_length=200, default=1)
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "initiatives"

    def clean(self):
        if self.start_date == None or self.end_date == None:
            raise ValidationError(
            'The start date or the end date cannot be undefined'
        )
        elif self.start_date > self.end_date:
            raise ValidationError(
      'The start date cannot be greater than the end date'
    )

class RiskCategory(models.Model):
    likelihood = models.PositiveIntegerField(choices=RISK_CHOICES, default=None)
    impact = models.PositiveIntegerField(choices=RISK_CHOICES, default=None)
    risk_category = models.CharField(max_length = 8, choices=RISK_CATEGORY_CHOICES, default=None)

    class JSONAPIMeta:
        resource_name = "riskcategories"
    
    def __str__(self):
        return self.risk_category


class RiskMitigationStrategy(models.Model):
    name =  models.CharField(max_length=100, blank=False)
    description = models.TextField()

    
    def __str__(self):
        return self.name

        
class Risk(models.Model):
    # We want to enforce risks on initiatives, but there will be general risks not tied to a programme. 
    # Thus for future reference it may be a good idea to somehow differentiate general cross-programme 
    # risks and specific ones. Perhaps either a boolean flag or having a risk interface with two implementations
    initiatives = models.ManyToManyField(Initiative, related_name='initiative_risks', blank=True) 
    
    name = models.CharField(blank=False, max_length=200)
    description = models.CharField(blank=False, max_length=200)
    likelihood = models.PositiveIntegerField(
        choices = RISK_CHOICES,
        default=R_VERY_LOW,
    )
    impact = models.PositiveIntegerField(
        choices = RISK_CHOICES,
        default=R_VERY_LOW,
    )
    flagged = models.BooleanField(default=False)
    risk_category = models.OneToOneField(RiskCategory, on_delete=models.CASCADE)
    mitigations = models.ManyToManyField(RiskMitigationStrategy, related_name='risks')
    

    

    def __str__(self):
        return self.name
    
    class Meta():
        db_table = "risk"

    class JSONAPIMeta:
        resource_name = "risks"






class Benefit(models.Model):
    goals = models.ManyToManyField(Goal, related_name='benefits')
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='prp/benefits/images')
    value = models.CharField(blank=False, max_length=12)


 

    priority = models.CharField(
        max_length = 8,
        choices = PRIORITY_CHOICES,
        default = UNKNOWN,
    )
    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "benefits"

    class Meta():
        db_table = "benefit"


class Target(models.Model):
    name = models.CharField(blank=False, max_length=200)
    benefits = models.ManyToManyField(Benefit, related_name='targets')
    description = models.TextField()
    outputs = models.ManyToManyField(Outcome, related_name='targets')
    achieved = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "targets"





class Milestone(models.Model):
    # project = models.ForeignKey(Project, related_name='milestones', on_delete=models.CASCADE)
    milestone_status = models.ForeignKey(MilestoneStatus, related_name='milestones', on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    date = models.DateField(datetime.date.today(), blank=False)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "milestones"


class MilestoneHistory(models.Model):
    milestone = models.ForeignKey(Milestone, related_name='milestone_histories', on_delete=models.CASCADE)
    from_status = models.ForeignKey(MilestoneStatus, on_delete=models.CASCADE, related_name = 'milestone_from_histories') 
    to_status = models.ForeignKey(MilestoneStatus, on_delete=models.CASCADE, related_name = 'milestone_to_histories')
    description = models.TextField()
    date = models.DateField(blank=False)
    
    class Meta():
        db_table = "milestone_history"

    def __str__(self):
        return '%s - %s.' % (self.date, self.description[0:99])

    class JSONAPIMeta:
        resource_name = "milestonehistories"





class Deliverable(models.Model):

    CHOICES = (
        (NO_IMPACT, 'None'),
        (LOW_IMPACT, 'Low'),
        (MODERATE_IMPACT, 'Moderate'),
        (SEVERE_IMPACT, 'Severe')
    )

    
    name = models.CharField(blank=False, max_length=200)
    description = models.TextField()
    end_date = models.DateField(validators=[validate_date_not_in_past], blank=False)
    progress = models.FloatField(validators=[validate_progress])
    team_impact = models.CharField(max_length = 8, choices=CHOICES, default=NO_IMPACT)
    sponsor_impact = models.CharField(max_length = 8, choices = CHOICES, default=NO_IMPACT)
    pm_impact = models.CharField(max_length = 8, choices = CHOICES, default=NO_IMPACT)
    order = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length = 12, choices = STATUS_CHOICES, default=NOT_STARTED)
    status_message = models.CharField(blank=False, max_length=200, default="No description")
    initiative = models.ForeignKey(Initiative, related_name="deliverables", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class JSONAPIMeta:
        resource_name = "deliverables"


class Update(models.Model):
    log = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(datetime.date.today(), validators=[validate_date_not_in_future], blank=False)
    author = models.ForeignKey(TeamMember, related_name="updates", on_delete=models.CASCADE)
    deliverable = models.ForeignKey(Deliverable, related_name="updates", on_delete=models.CASCADE)
    def __str__(self):
        return self.description

    class JSONAPIMeta:
        resource_name = "updates"




class Role(models.Model):
    team_members = models.ManyToManyField(TeamMember, related_name='roles')
    projects = models.ManyToManyField(Project, related_name='roles')
    role = models.CharField(max_length = 20, choices=ROLE_CHOICES, default=NO_ROLE)

    class JSONAPIMeta:
        resource_name = "roles"

    def __str__(self):
        return self.role



# MUST place this after the Update model declaration to avoid circular dependencies
from .utils import generate_update_log


models.signals.pre_save.connect(validate_impact_choice, sender=Deliverable)
models.signals.post_save.connect(generate_update_log, sender=Deliverable)


