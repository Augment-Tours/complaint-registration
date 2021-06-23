from django.urls import include, path, re_path
from rest_framework import routers
from .views import TestView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^test/$', TestView.as_view(), name='test'),
]