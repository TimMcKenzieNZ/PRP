from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.core.exceptions import ValidationError
from django.db.utils import DataError
from rest_framework import mixins
from django.shortcuts import render
from django.http import HttpResponse

# Rest framework related imports
from rest_framework import generics, renderers, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route
from rest_framework import status

# Our project related imports
from programmes.models import *
from programmes.serializers import *




class ProblemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Problem Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Problem.objects.all().order_by('id')
    serializer_class = ProblemSerializer



class GoalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Objective Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Goal.objects.all().order_by('id')
    serializer_class = GoalSerializer
    filterset_fields = ('id','programme','benefits')



class ProgrammeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Programme Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Programme.objects.all().order_by('id')
    serializer_class = ProgrammeSerializer
    filterset_fields = ('id', 'goals', 'slug')


    """
    Gets all the goals of a programme in a single request
    """
    @detail_route() # read-only GET method
    def goals(self, request, pk=None):
        programme = self.get_object()
        serializer = GoalSerializer(programme.goals.all(), context={'request': request}, many=True)
        return Response(serializer.data)



class InitiativeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Initiative Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Initiative.objects.all().order_by('id').distinct()
    serializer_class = InitiativeSerializer
    filterset_fields = ('id','projects__goals__programme')

    @detail_route() # read-only GET method
    def deliverables(self, request, pk=None):
        initiative = self.get_object()
        serializer = DeliverableSerializer(initiative.deliverables.all(), context={'request': request}, many=True)
        return Response(serializer.data)
    
    @detail_route() # read-only GET method
    def risks(self, request, pk=None):
        initiative = self.get_object()
        serializer = RiskSerializer(initiative.risks.all(), context={'request': request}, many=True)
        return Response(serializer.data)

    @detail_route() # read-only GET method
    def roles(self, request, pk=None):
        initiative = self.get_object()
        serializer = RoleSerializer(initiative.roles.all(), context={'request': request}, many=True)
        return Response(serializer.data)


class StakeholderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Stakeholder Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Stakeholder.objects.all().order_by('id')
    serializer_class = StakeholderSerializer



class OutcomeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Outcome Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Outcome.objects.all().order_by('id')
    serializer_class = OutcomeSerializer




class TargetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Target Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Target.objects.all().order_by('id')
    serializer_class = TargetSerializer



class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Team Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Team.objects.all().order_by('id')
    serializer_class = TeamSerializer



class MilestoneViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Milestone Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Milestone.objects.all().order_by('id')
    serializer_class = MilestoneSerializer



class MilestoneStatusViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Milestone Status Viewset which only provides 'list' and 'detail' actions
    """
    queryset = MilestoneStatus.objects.all().order_by('id')
    serializer_class = MilestoneStatusSerializer



class MilestoneHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Milestone history Viewset which only provides 'list' and 'detail' actions
    """
    queryset = MilestoneHistory.objects.all().order_by('id')
    serializer_class = MilestoneHistorySerializer


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Team member Viewset which only provides 'list' and 'detail' actions
    """
    queryset = TeamMember.objects.all().order_by('id')
    serializer_class = TeamMemberSerializer



class BenefitViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Benefit Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Benefit.objects.all().order_by('id').distinct()
    serializer_class = BenefitSerializer
    filterset_fields = ('id','goals__programme')



class DeliverableViewAndUpdateSet(viewsets.GenericViewSet,
                                mixins.UpdateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin):
    """
    Deliverable Viewset which only provides 'list', 'update', and 'detail' actions
    """
    queryset = Deliverable.objects.all().order_by('id').distinct()
    serializer_class = DeliverableSerializer
    filterset_fields = ('id','initiative__projects__goals__programme')

    """
        Performs an update of the deliverable and creates an instance of an update log
        Request body should be in the following layout:
        {
            "data" : {
                "type": "deliverables",
                "id": int,
                "attributes": {
                    "progress": float,
                    "order": int,
                    "name": string,
                    "end_date": string(YYYY-MM-DD),
                    "description": string,
                    "initiative": string(http://localhost:8000/api/initiatives/int),
                    "sponsor_impact": string(none, low, moderate, severe),
                    "pm_impact": string(none, low, moderate, severe),
                    "team_impact": string(none, low, moderate, severe),
                    "updateData": {
                        "data" : {
                            "type": "updates",
                            "id": null,
                            "attributes": {
                                "description": string,
                                "date": string(YYYY-MM-DD),
                                "log": string,
                                "author": string(http://localhost:8000/api/team_members/int),
                                "deliverable": string(http://localhost:8000/api/deliverables/int)
                            }
                        }
                    }
                }
            }
        }
    """
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        deliverableSerializer = DeliverableSerializer(instance, request.data, context={'request': request})
        deliverableSerializer.is_valid(raise_exception=True)
        updateSerializer = UpdateSerializer(data=request.data["updateData"]["data"]["attributes"], context={'request': request})
        updateSerializer.is_valid(raise_exception=True)
        try :
            deliverableSerializer.save()
            updateSerializer.save()
        except ValidationError as error:
            return HttpResponseBadRequest(error)
        return Response(deliverableSerializer.data)

    


class RiskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Risk Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Risk.objects.all().order_by('id')
    serializer_class = RiskSerializer
    @detail_route() # read-only GET method
    def mitigations(self, request, pk=None):
        risk = self.get_object()
        serializer = RiskMitigationStrategySerializer(risk.mitigations.all(), context={'request': request}, many=True)
        return Response(serializer.data)


class RiskCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Risk Category Viewset which only provides 'list' and 'detail' actions
    """
    queryset = RiskCategory.objects.all().order_by('id')
    serializer_class = RiskCategorySerializer


class RiskMitigationStrategyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    RiskMitigationStrategy Viewset which only provides 'list' and 'detail' actions
    """
    queryset = RiskMitigationStrategy.objects.all().order_by('id')
    serializer_class = RiskMitigationStrategySerializer


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Role Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Project Viewset which only provides 'list' and 'detail' actions
    """
    queryset = Project.objects.all().order_by('id').distinct() # Distinct() required when filtering were a project is attached to multiple goals
    serializer_class = ProjectSerializer
    filterset_fields = ('id', 'goals__programme') # goals_programme filters along relational paths, in this case, for each goal of a project it checks the goal.programme attribute


class StatusMessageCreateOrListOrRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """
    Update Viewset which provides 'create', 'retrieve', and 'list' actions
    """
    queryset = Update.objects.all().order_by('id')
    serializer_class = UpdateSerializer

