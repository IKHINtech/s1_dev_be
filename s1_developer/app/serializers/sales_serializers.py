from rest_framework import serializers

from s1_developer.app.models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['sales_name']
