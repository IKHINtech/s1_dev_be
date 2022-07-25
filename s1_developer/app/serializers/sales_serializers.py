from rest_framework import serializers

from s1_developer.app.models import Sales
from s1_developer.app.services.ax_services import AXServicess


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['sales_name']

    def get_list(self, url, page, no_page, project_code):
        data = AXServicess().get_list_sales(project_code=project_code, pages=page, no_page=no_page)
        if no_page == True:
            if isinstance(data.json(), list) and data.status_code == 200:
                response_data = [{'sales_name': e['SalesName']} for e in data.json()]
            return response_data
        else:
            if isinstance(data.json(), list) and data.status_code == 200:
                response_data = []

                for e in data.json():
                    response_data.append(
                        {
                            "sales_name": e['SalesName']
                        }
                    )

            data = {
                'next': None if len(response_data) < 10 else url.replace(f'pages={page}', f'pages={page+1}'),
                'result': response_data
            }

        return data
