from django.urls import re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    re_path(r'^token-auth/$', TokenObtainPairView.as_view()),
    re_path(r'^token-refresh/$', TokenRefreshView.as_view()),

    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
]