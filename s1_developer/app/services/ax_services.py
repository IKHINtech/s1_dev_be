import requests
from requests.auth import HTTPBasicAuth


class AXServicess():
    def get_list_project(self, pages=1, no_page=False):
        body = {
            'UserID': 'bastian.hadiwirawan@agungsedayu.com',
            'Page': pages
        }

        if no_page == True:
            body['Page'] = 0

        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600'
        }
        ax_url = f"http://103.87.78.207:8085/api/rva/GetListProject"
        response = requests.post(ax_url, json=body, auth=HTTPBasicAuth(
            'USERdevapiVAR.agungsedayu.com', 'PASSdevapiVAR.agungsedayu.com'))
        return response

    def get_list_sales(self, project_code, pages=1, no_page=False):
        body = {
            "ProjectId": project_code,
            'UserID': 'bastian.hadiwirawan@agungsedayu.com',
            "Page": pages
        }
        if no_page == True:
            body['Page'] = 0

        ax_url = f"http://103.87.78.207:8085/api/rva/GetListSales"
        response = requests.post(ax_url, json=body, auth=HTTPBasicAuth(
            'USERdevapiVAR.agungsedayu.com', 'PASSdevapiVAR.agungsedayu.com'))
        return response

    def reserve_va(self, project_code, description, customer_name):
        body = {
            "ProjectId": project_code,
            "CustName": customer_name,
            "Description": description,
            "UserId": 'bastian.hadiwirawan@agungsedayu.com',
        }
        ax_url = "http://103.87.78.207:8085/api/rva/request"
        response = requests.post(ax_url, json=body, auth=HTTPBasicAuth(
            'USERdevapiVAR.agungsedayu.com', 'PASSdevapiVAR.agungsedayu.com'))

        return response

    def list_reserved_va(self, project_code, start_date, end_date, sales, pages):
        body = {
            "ProjectID": project_code,
            "FromDate": start_date.strftime('%d/%m/%Y'),
            "ToDate": end_date.strftime('%d/%m/%Y'),
            "SalesName": sales,
            "UserId": 'bastian.hadiwirawan@agungsedayu.com',
            "Page": pages,
        }
        ax_url = f"http://103.87.78.207:8085/api/rva/Inquiries"
        response = requests.post(ax_url, json=body, auth=HTTPBasicAuth(
            'USERdevapiVAR.agungsedayu.com', 'PASSdevapiVAR.agungsedayu.com'))

        return response
