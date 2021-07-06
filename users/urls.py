from django.urls import re_path, include
from .views import LoggedInUserApiView, SignupUserApiView

urlpatterns = [
    re_path(r'^signup/$', SignupUserApiView().as_view(), name='logged_in_user_profile'),
    re_path(r'^profile/$', LoggedInUserApiView().as_view(), name='logged_in_user_profile'),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
]