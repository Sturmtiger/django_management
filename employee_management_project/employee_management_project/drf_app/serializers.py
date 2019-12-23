from rest_framework import serializers
from management_app import models


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manager
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Job
        fields = '__all__'


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WorkPlace
        fields = '__all__'


class WorkPlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WorkPlace
        fields = '__all__'


class WorkTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.WorkTime
        fields = '__all__'


class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Statistics
        fields = '__all__'