from s1_developer.app.models import Project
from s1_developer.app.serializers.project_serializers import ProjectSerializer
from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        data = request
        return super().list(request, *args, **kwargs)
