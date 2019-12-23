from rest_framework import viewsets
from management_app import models
from .serializers import (CompanySerializer, ManagerSerializer, EmployeeSerializer,
                          JobSerializer, WorkPlaceSerializer, WorkTimeSerializer,
                          StatisticsSerializer,)

# Create your views here.


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = CompanySerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = models.Manager.objects.all()
    serializer_class = ManagerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = EmployeeSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = JobSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):
    queryset = models.WorkPlace.objects.all()
    serializer_class = WorkPlaceSerializer


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = models.WorkTime.objects.all()
    serializer_class = WorkTimeSerializer


class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = models.Statistics.objects.all()
    serializer_class = StatisticsSerializer