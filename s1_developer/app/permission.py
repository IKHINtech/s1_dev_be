from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import (BaseAuthentication,
                                           get_authorization_header)

from s1_developer.app.services.oauth_service import OauthService


def get_token_header(request):
    auth_header = get_authorization_header(request).split()

    if not auth_header or auth_header[0].lower() != 'bearer'.encode():
        return None

    if len(auth_header) == 1:
        msg = 'Invalid token. No credentials provided.'
        raise exceptions.AuthenticationFailed(msg)
    elif len(auth_header) > 2:
        msg = 'Invalid token. Token string should not contain spaces.'
        raise exceptions.AuthenticationFailed(msg)

    try:
        token = auth_header[1].decode()
        return token
    except UnicodeError:
        msg = 'Invalid token. Token string should not contain invalid characters.'
        raise exceptions.AuthenticationFailed(msg)


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = get_token_header(request)
        # r = OauthService().check_token(token)

        # if r is None or 'authorities' not in r:
        #     raise exceptions.NotAuthenticated

        # try:
        user = type('ReturnObject', (), {})()
        # [setattr(user, )]

        # except Exception as e:
        #     raise exceptions.AuthenticationFailed('User Not Found')

        return (user, token)
