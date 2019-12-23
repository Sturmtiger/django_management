from rest_framework import serializers
from management_app.models import (Company, Manager, Employee, Job,
                                   WorkPlace, WorkTime, Statistics,)


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'name', 'weekly_hours_limit']


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['url', 'company', 'name', 'email']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'name']


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['url', 'company', 'name']


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ['url', 'job', 'employee', 'status']


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ['url', 'job', 'employee', 'status']


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkTime
        fields = ['url', 'workplace', 'date', 'hours_worked']


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistics
        fields = ['url', 'workplace', 'hours_total', 'timestamp']