"""employee_management_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .drf_app import views


# DRF API config
router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'managers', views.ManagerViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'workplaces', views.WorkPlaceViewSet)
router.register(r'worktimes', views.WorkTimeViewSet)
router.register(r'statistics', views.StatisticsViewSet)

urlpatterns = [
    path('', include('management_app.urls', namespace='management_app')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
