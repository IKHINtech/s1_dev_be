from rest_framework.viewsets import ModelViewSet
from s1_developer.app.models import Sales
from s1_developer.app.serializers.sales_serializers import SalesSerializer


class SalesViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        data = request
        return super().list(request, *args, **kwargs)
