from rest_framework import serializers
from management_app.models import (Company, Manager, Employee, Job,
                                   WorkPlace, WorkTime, Statistics,)


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Manager
        fields = ('url', 'company_name', 'company', 'name', 'email')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    managers = ManagerSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('url', 'name', 'weekly_hours_limit', 'managers')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('url', 'name',)


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('url', 'company', 'name',)


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ('url', 'job', 'employee', 'status',)


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ('url', 'job', 'employee', 'status',)


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkTime
        fields = ('url', 'workplace', 'date', 'hours_worked',)


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistics
        fields = ('url', 'workplace', 'hours_total', 'timestamp',)


class StatisticsUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistics
        fields = ('url', 'workplace', 'hours_total', 'timestamp',)
        read_only_fields = ('workplace',)