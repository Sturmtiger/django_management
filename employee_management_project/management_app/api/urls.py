from rest_framework import routers
from management_app.api import views


router = routers.DefaultRouter()

router.register(r'companies', views.CompanyViewSet)
router.register(r'managers', views.ManagerViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'workplaces', views.WorkPlaceViewSet)
router.register(r'worktimes', views.WorkTimeViewSet)
router.register(r'statistics', views.StatisticsViewSet)
