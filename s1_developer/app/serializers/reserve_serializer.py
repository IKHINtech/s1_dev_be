from rest_framework import serializers

from s1_developer.app.models import Reserve


class ReserveSerializer(serializers.Serializer):
    project_code = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    sales = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        models = Reserve
        fields = '__all__'

    def get_reserve(self, validated_data):
        data = Reserve.objects.filter(
            project_code__project_code=validated_data['project_code'],
            request_date__gte=validated_data['start_date'],
            request_date__lte=validated_data['end_date']
        )
        return data


class ReturnReserve(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        exclude = ['id']
