from rest_framework import serializers
from .models import OPProject, WorkPackage

class WorkPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPackage
        fields = [
            'openproject_id',
            'subject',
            'status',
            'assignee',
            'updated_at',
        ]
        depth = 1

class ProjectSerializer(serializers.ModelSerializer):
    open_packages = serializers.IntegerField()
    closed_packages = serializers.IntegerField()

    class Meta:
        model = OPProject
        fields = ['openproject_id', 'name', 'identifier', 'open_packages', 'closed_packages']
