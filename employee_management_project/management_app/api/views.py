from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from management_app.models import (Company, Manager, Employee, Job,
                                   WorkPlace, WorkTime, Statistics,)
from .serializers import (CompanySerializer, ManagerSerializer, EmployeeSerializer,
                          JobSerializer, WorkPlaceSerializer, WorkTimeSerializer,
                          StatisticsSerializer,)


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):
    queryset = WorkPlace.objects.all()
    serializer_class = WorkPlaceSerializer


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer


class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

    @action(detail=False)
    def hours_descend(self, request):
        statistics_hours_descend = Statistics.objects.all().order_by('-hours_total')

        page = self.paginate_queryset(statistics_hours_descend)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(statistics_hours_descend, many=True)
        return Response(serializer.data)
