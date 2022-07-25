from tkinter.tix import Tree

from django.http import JsonResponse
from rest_framework.response import Response
from s1_developer.app.models import Reserve
from rest_framework import viewsets

from s1_developer.app.serializers.create_reserve_serializer import CreateReserveSerializer
from s1_developer.app.serializers.reserve_serializer import ReturnReserve


class CreateReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = CreateReserveSerializer
    permission_classes = []
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.validated_data)

        return Response(data)
