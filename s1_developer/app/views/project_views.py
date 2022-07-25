import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from s1_developer.app.models import Project
from s1_developer.app.serializers.project_serializers import ProjectSerializer
from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        pages = request.query_params.get('page', None)
        no_page = True if request.query_params.get('no_page', None) == '' else False
        url = request.build_absolute_uri()
        serializer = self.get_serializer()
        data = serializer.get_list(url=url, page=pages, no_page=no_page)
        return Response(data)
