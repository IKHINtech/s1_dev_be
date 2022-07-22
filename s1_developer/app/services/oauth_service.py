import requests
from django.conf import settings


class OauthService:
    def check_token(self, token):
        url = settings.OAUTH2_URL + 'oauth/check_token/'
        headers = {'Authorization': f'Bearer {settings.OAUTH2_TOKEN}'}
        body = {'token': token}

        response = requests.post(url=url, headers=headers, data=body)
        if response.status_code == 200:
            r = response.json()
            if r['active'] == False:
                return None
            else:
                return r
        else:
            return None

    def get_user_by_email_and_mobile_no(self, email, phone=None):
        url = f'{settings.OAUTH2_URL}api/users/byemailormobile/{email}'
        url = url if phone is None else url + '/' + phone
        headers = {'Authorization': f'Bearer {settings.OAUTH2_TOKEN}'}

        response = requests.get(url=url, headers=headers)
        return response.json()['data'] if response.json()['data'] != None else {'detail': ''}

    def create_oauth_user(self, body):
        url = f'{settings.OAUTH2_URL}api/users/'
        headers = {'Authorization': f'Bearer {settings.OAUTH2_TOKEN}'}

        response = requests.post(url=url, json=body, headers=headers)
        if 200 <= response.status_code <= 299:
            return response.json()['data']
        else:
            return None

    def update_oauth_user(self, body, oauth_id):
        url = f'{settings.OAUTH2_URL}api/users/{oauth_id}/'
        headers = {'Authorization': f'Bearer {settings.OAUTH2_TOKEN}'}

        response = requests.put(url=url, json=body, headers=headers)
        if 200 <= response.status_code <= 299:
            return response.json()['data']
        else:
            return None

    def get_user_by_id(self, oauth_id):
        url = f'{settings.OAUTH2_URL}api/users/{oauth_id}/'

        headers = {'Authorization': f'Bearer {settings.OAUTH2_TOKEN}'}

        response = requests.get(url, headers=headers)
        return response.json()['data'] if response.json()['data'] != None else {'detail': ''}
