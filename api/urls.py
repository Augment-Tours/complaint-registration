from django.urls import re_path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import CreateFeedbackApiView, ListOwnedFeedbackApiView, UpdateFeedbackApiView

urlpatterns = [
    re_path(r'^token-auth/$', obtain_jwt_token),
    re_path(r'^token-refresh/$', refresh_jwt_token),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    
    re_path(r'^feedback/create/', CreateFeedbackApiView.as_view(), name='create-feedback'),
    re_path(r'^feedback/list/', ListOwnedFeedbackApiView.as_view(), name='list-feedback'),
    # update endpoint
    re_path(r'^feedback/update/(?P<pk>\d+)/$', UpdateFeedbackApiView.as_view(), name='update-feedback'),
]