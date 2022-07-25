from rest_framework import serializers
import random
from s1_developer.app.services.ax_services import AXServicess


from s1_developer.app.models import Project, Reserve


class CreateReserveSerializer(serializers.Serializer):
    project_code = serializers.CharField()
    description = serializers.CharField()
    customer_name = serializers.CharField()

    class Meta:
        db_table = Reserve
        fields = ['project_code', 'description', 'customer_name']

    def create(self, validated_data):
        response = AXServicess().reserve_va(
            project_code=validated_data['project_code'],
            customer_name=validated_data['customer_name'],
            description=validated_data['description']
        )
        if isinstance(response.json(), list) and response.status_code == 200:
            response_data = {
                'va_code': response.json()[0]['NoVA'],
                'project_code': response.json()[0]['Project'],
                'customer_name': response.json()[0]['CustName'],
                'description': response.json()[0]['Description'],
            }

        return response_data
