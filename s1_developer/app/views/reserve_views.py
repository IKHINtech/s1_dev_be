from django.http import JsonResponse
from s1_developer.app.models import Reserve
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from s1_developer.app.serializers.create_reserve_serializer import CreateReserveSerializer


from s1_developer.app.serializers.reserve_serializer import ReserveSerializer, ReturnReserve


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = []
    # http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = ReserveSerializer(data=self.request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        data = serializer.get_reserve(serializer.validated_data)
        return_data = ReturnReserve(data, many=True)
        # data = list(data.values())

        return JsonResponse(return_data.data, safe=False)

    def list(self, request, *args, **kwargs):
        project_code = request.query_params.get('project_code', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        sales = request.query_params.get('sales', None)
        pages = request.query_params.get('pages', None)
        serializer = self.get_serializer()
        url = request.build_absolute_uri()
        data = serializer.get_list(url=url, pages=pages, project_code=project_code, start_date=start_date,
                                   end_date=end_date, sales=sales)
        return Response(data)
