from django.urls import re_path, include
from .views import LoggedInUserApiView

urlpatterns = [
    re_path(r'^profile/$', LoggedInUserApiView().as_view(), name='logged_in_user_profile'),
]