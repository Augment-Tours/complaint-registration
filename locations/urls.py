from django.urls import include, path, re_path
from rest_framework import routers
from .views import CreateCountryApiView

urlpatterns = [
    re_path(r'^country/create/$', CreateCountryApiView().as_view(), name='create_country'),
]