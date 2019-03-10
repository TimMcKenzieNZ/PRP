from django.contrib.auth.models import User
from rest_framework import serializers


from programmes.models import *

class RiskCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = RiskCategory
        fields = ('id', 'likelihood', 'impact', 'risk_category')


class RiskMitigationStrategySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskMitigationStrategy
        fields = ('id', 'name', 'description')


class RiskSerializer(serializers.ModelSerializer):
    included_serializers = {
        'riskmitigationstratgey': RiskMitigationStrategySerializer
    }

    mitigations = RiskMitigationStrategySerializer(many=True, read_only=True)
    
    risk_mitigations = serializers.SerializerMethodField()

    """ Gets the risk severity of the associated risk_category when the risk gets itself """
    def get_risk_mitigations(self, obj):
        mitigations_list = []
        mitigations_queryset = obj.mitigations.get_queryset()
        for mitigation in mitigations_queryset:
            mitigations_list.append({"name": mitigation.name, "description": mitigation.description})
        return mitigations_list


    risk_severity = serializers.SerializerMethodField()

    """ Gets the risk severity of the associated risk_category when the risk gets itself """
    def get_risk_severity(self, obj):
        return obj.risk_category.risk_category

   
    class Meta:
        model = Risk
        fields = ('id', 'name', 'description', 'likelihood', 'impact', 'flagged', 'risk_category', 'risk_severity', 'risk_mitigations', 'mitigations', 'initiatives')




class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    goals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='goal-detail')
    class Meta:
        model = Problem
        fields = ('id', 'name', 'description', 'order', 'goals')





class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    roles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='role-detail')
    updates = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='update-detail')
    programmes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='programme-detail')
    class Meta:
        model = TeamMember
        fields = ('id', 'email', 'position', 'first_name', 'last_name', 'contact_number', 'image', 'roles', 'updates', 'programmes')



class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    #author = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='teammember-detail')
    #deliverable = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='deliverable-detail')
    included_serializers = {
        'author': TeamMemberSerializer
    }
    class Meta:
        model = Update
        fields = ('id', 'description', 'date', 'log', 'author', 'deliverable')
        

class DeliverableSerializer(serializers.HyperlinkedModelSerializer):
    updates = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='update-detail')
    included_serializers = {
        'updates': UpdateSerializer
    }
    class Meta:
        model = Deliverable
        fields = ('id', 'name', 'description', 'progress', 'order', 'updates', 
        'team_impact', 'sponsor_impact', 'pm_impact', 'status', 'status_message', 'end_date', 'initiative')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
   # team_members = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='teammember-detail')

    included_serializers = {
        'team_members': TeamMemberSerializer
    }

    class Meta:
        model = Role
        fields = ('id', 'team_members', 'projects', 'role')




class InitiativeSerializer(serializers.HyperlinkedModelSerializer):
    deliverables = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='deliverable-detail')
    #risks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='risk-detail')


    included_serializers = {
        'deliverables': DeliverableSerializer,
        'risks': RiskSerializer
    }

    class Meta:
        # milestones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='milestone-detail')
        model = Initiative
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 
        'progress', 'order', 'status', 'deliverables', 'risks', 'projects')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    roles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='role-detail') # DON'T change role to role, the server will cry
    initiatives = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='initiative-detail')

    included_serializers = {
        'roles': RoleSerializer,
        'initiatives': InitiativeSerializer
    }

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 
        'progress', 'priority', 'cost', 'image', 'goals', 'status', 'initiatives', 'roles')


class TargetSerializer(serializers.HyperlinkedModelSerializer):
    # initiatives = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='initiative-detail')
    class Meta:
        model = Target
        fields = ('id', 'name', 'description', 'achieved', 'date', 'benefits')


class BenefitSerializer(serializers.HyperlinkedModelSerializer):
    
    targets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='target-detail')

    included_serializers = {
        'targets': TargetSerializer,
    }
    
    class Meta:
        model = Benefit
        fields = ('id', 'name', 'description', 'image', 'value', 'priority', 'goals', 'targets')

        
class GoalSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='project-detail')
    benefits = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='benefit-detail')
    included_serializers = {
        'projects': ProjectSerializer,
        'benefits': BenefitSerializer
    }
    class Meta:
        model = Goal
        fields = ('id', 'name', 'description', 'image', 'order', 'problems', 'programme', 'benefits', 'projects')


class ProgrammeSerializer(serializers.HyperlinkedModelSerializer):
    goals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='goal-detail')

    # For simplifiyng requests, a  GET programme request returns its goals too
    included_serializers = {
        'goals': GoalSerializer
    }
    class Meta:
        model = Programme
        fields = ('id', 'name', 'description', 'image', 'goals', 'start_date', 'end_date', 
        'vision', 'slug', 'url', 'members') # Don't forget to include the url field if using slugs

        # The following replaces the programme id with the programme slug in the URL, making it more human readable
        # e.g. 'programmes/1/' becomes 'programmes/Student_First_Programme/'
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'}
        # }




class StakeholderSerializer(serializers.HyperlinkedModelSerializer):
    # initiatives = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='initiative-detail')
    class Meta:
        model = Stakeholder
        fields = ('id', 'name', 'description', 'contact_name', 'contact_email')



class OutcomeSerializer(serializers.HyperlinkedModelSerializer):
    initiatives = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='initiative-detail')
    targets = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='target-detail')
    class Meta:
        model = Outcome
        fields = ('id', 'name', 'description', 'pros', 'cons', 'date', 'targets', 'initiatives')






class MilestoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Milestone
        fields = ('id', 'name', 'description', 'date', 'milestone_status')



class TeamSerializer(serializers.HyperlinkedModelSerializer):
    # initiatives = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='initiative-detail')
    #team_members = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='teammember-detail')
    class Meta:
        model = Team
        fields = ('id', 'name', 'description')



class MilestoneStatusSerializer(serializers.HyperlinkedModelSerializer):
    milestones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='milestone-detail')
    milestone_from_histories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='milestonehistory-detail')
    milestone_to_histories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='milestonehistory-detail')
    class Meta:
        model = MilestoneStatus
        fields = ('id', 'name', 'description', 'status', 'milestones', 'milestone_from_histories', 'milestone_to_histories')



class MilestoneHistorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = MilestoneHistory
        fields = ('id', 'description', 'from_status', 'to_status', 'date', 'milestone')















