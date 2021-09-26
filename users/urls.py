from django.urls import re_path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# from .views import FirebaseLogin, ConnectToFacebook
from .views import ListUsersApiView, ToggleUserStatusApiView

urlpatterns = [
    re_path(r'^all/$', ListUsersApiView.as_view(), name='user-list'),
    # toggle a users status (active/inactive)
    re_path(r'^toggle-status/(?P<pk>\d+)/$', ToggleUserStatusApiView.as_view(), name='toggle-user-status'),
]