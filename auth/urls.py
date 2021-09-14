from django.urls import re_path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import FirebaseLogin, ConnectToFacebook

urlpatterns = [
    re_path(r'^token-auth/$', obtain_jwt_token),
    re_path(r'^token-refresh/$', refresh_jwt_token),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^rest-auth/firebase/$', FirebaseLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/link-to-facebook/$', ConnectToFacebook.as_view(), name='')
]