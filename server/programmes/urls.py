from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from programmes import views


router = DefaultRouter(trailing_slash=False) # this removes the last slash from the URL path (apparantly this confuses Ember data)
router.register(r'problems',views.ProblemViewSet)
router.register(r'goals',views.GoalViewSet)
router.register(r'programmes',views.ProgrammeViewSet)
router.register(r'initiatives',views.InitiativeViewSet)
router.register(r'stakeholders',views.StakeholderViewSet)
router.register(r'outcomes',views.OutcomeViewSet)
router.register(r'targets',views.TargetViewSet)
router.register(r'teams',views.TeamViewSet)
router.register(r'milestones',views.MilestoneViewSet)
router.register(r'milestone_statuses',views.MilestoneStatusViewSet)
router.register(r'milestone_histories',views.MilestoneHistoryViewSet)
router.register(r'team_members',views.TeamMemberViewSet)
router.register(r'benefits', views.BenefitViewSet)
router.register(r'deliverables', views.DeliverableViewAndUpdateSet)
router.register(r'risks', views.RiskViewSet)
router.register(r'risk_categories', views.RiskCategoryViewSet)
router.register(r'risk_mitigation_strategies', views.RiskMitigationStrategyViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'updates', views.StatusMessageCreateOrListOrRetrieveViewSet)




urlpatterns = [
    url('', include(router.urls)),



]
