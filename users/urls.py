from django.urls import re_path
from .views import LoggedInUserView

urlpatterns = [
    re_path(r'^profile/$', LoggedInUserView().as_view(), name='logged_in_user_profile'),
]