from django.urls import re_path, include
from .views import LoggedInUserApiView, UpdateUserApiView, SearchUserApiView

urlpatterns = [
    re_path(r'^profile/$', LoggedInUserApiView().as_view(), name='logged_in_user_profile'),
    re_path(r'^update/(?P<pk>\d+)/$', UpdateUserApiView().as_view(), name='update_user'),
    re_path(r'^search/$', SearchUserApiView().as_view(), name='search_user'),
    
]