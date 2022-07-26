from rest_framework import serializers
from datetime import datetime

from s1_developer.app.models import Reserve
from s1_developer.app.services.ax_services import AXServicess


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

    def get_list(self, url, project_code, start_date, end_date, sales, pages):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        response = AXServicess().list_reserved_va(project_code=project_code,
                                                  start_date=start_date,
                                                  end_date=end_date,
                                                  sales=sales,
                                                  pages=pages)
        if isinstance(response.json(), list) and response.status_code == 200:
            response_data = []

            for e in response.json():
                req_date = None
                trans_date = None

                try:
                    req_date = datetime.strptime(e['ReqDate'], '%d/%m/%Y')
                    req_date = req_date.strftime('%Y-%m-%d')
                except Exception as exc:
                    req_date = None

                try:
                    trans_date = datetime.strptime(e['Transdate'], '%d/%m/%Y')
                    trans_date = trans_date.strftime('%Y-%m-%d')
                except Exception as exc:
                    trans_date = None

                response_data.append(
                    {
                        'project_code': e['Project'],
                        'va_code': e['NoVA'],
                        'request_date': req_date,
                        'sales': e['Sales'],
                        'customer_name': e['CustName'],
                        'description': e['Description'],
                        'amount': e['Amount'],
                        'transaction_date': trans_date,
                        'reservation_number': e['NoReservasi'],
                        'unit_code': e['UnitID'],
                    }
                )
        data = {
            'next': None if len(response_data) < 10 else url.replace(f'pages={int(pages)}', f'pages={int(pages)+1}'),
            'results': response_data,

        }
        return data


class ReturnReserve(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        exclude = ['id']
