from rest_framework import serializers

from s1_developer.app.models import Project


class ProjectSerializer(serializers.Serializer):
    project_code = serializers.CharField()
    project_name = serializers.CharField()

    class Meta:
        models = Project
        fields = '__all__'

    def create(self, validated_data):
        data = Project.objects.create(**validated_data)

        return data
