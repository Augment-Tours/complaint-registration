from django.urls import re_path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    re_path(r'^token-auth/$', obtain_jwt_token),
    re_path(r'^token-refresh/$', refresh_jwt_token),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]