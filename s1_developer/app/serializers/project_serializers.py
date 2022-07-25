from rest_framework import serializers

from s1_developer.app.models import Project
from s1_developer.app.services.ax_services import AXServicess


class ProjectSerializer(serializers.Serializer):
    project_code = serializers.CharField()
    project_name = serializers.CharField()

    class Meta:
        models = Project
        fields = '__all__'

    def create(self, validated_data):
        data = Project.objects.create(**validated_data)

        return data

    def get_list(self, url, page=1, no_page=False):
        data = AXServicess().get_list_project(page, no_page)

        if no_page == True:
            if isinstance(data.json(), list) and data.status_code == 200:
                response_data = [{'project_code': e['projectID'], 'project_name': e['projectName']}
                                 for e in data.json()]
            return response_data
        else:
            if isinstance(data.json(), list) and data.status_code == 200:
                response_data = []
                for e in data.json():
                    response_data.append(
                        {
                            "project_code": e['projectID'],
                            "project_name": e['projectName']
                        }
                    )

            data = {
                'next': None if len(response_data) < 10 else url.replace(f'pages={page}', f'pages={page+1}'),
                'result': response_data,
            }
            return data
