from django.urls import re_path, include
from .views import LoggedInUserApiView, UpdateUserApiView, SearchUserApiView, \
                    ListUsersApiView, GetUserProfileApiView, UpdateUserProfileApiView

urlpatterns = [
    re_path(r'^update/(?P<pk>\d+)/$', UpdateUserApiView().as_view(), name='update_user'),
    re_path(r'^search/$', SearchUserApiView().as_view(), name='search_user'),
    re_path(r'^all/$', ListUsersApiView().as_view(), name='list_user'),

    re_path(r'^profile/$', LoggedInUserApiView().as_view(), name='logged_in_user_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$', GetUserProfileApiView.as_view(), name='user_profile'),
    re_path(r'^profile/update/(?P<pk>\d+)/$', UpdateUserProfileApiView.as_view(), name='update_user_profile'),
]