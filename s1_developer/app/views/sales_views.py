from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ModelViewSet
from s1_developer.app.models import Sales
from s1_developer.app.serializers.sales_serializers import SalesSerializer
from rest_framework.response import Response


class SalesViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        pages = request.query_params.get('page', None)
        no_page = True if request.query_params.get('no_page', None) == '' else False
        project_code = request.query_params.get('project_code')
        if project_code == None:
            raise ValidationError({'error': 'project_code required'})
        url = request.build_absolute_uri()
        serializer = self.get_serializer()
        data = serializer.get_list(url=url, project_code=project_code, page=pages, no_page=no_page)
        return Response(data)
