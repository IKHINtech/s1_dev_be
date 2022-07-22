from rest_framework import serializers
import random


from s1_developer.app.models import Project, Reserve


class CreateReserveSerializer(serializers.Serializer):
    project_code = serializers.CharField()
    description = serializers.CharField()
    customer_name = serializers.CharField()

    class Meta:
        db_table = Reserve
        fields = ['project_code', 'description', 'customer_name']

    def create(self, validated_data):
        project = Project.objects.get(project_code=validated_data['project_code'])
        data = Reserve.objects.create(
            project_code=project,
            description=validated_data['description'],
            customer_name=validated_data['customer_name'],
            va_code=random.random())
        return data
