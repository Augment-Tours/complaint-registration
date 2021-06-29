from django.urls import include, path, re_path
from rest_framework import routers
from .views import CreateCountryApiView, CreateRegionApiView, EditCountryApiView, \
                    ListCountryApiView

urlpatterns = [
    re_path(r'^country/create/$', CreateCountryApiView().as_view(), name='create_country'),
    re_path(r'^country/edit/$', EditCountryApiView().as_view(), name='edit_country'),
    re_path(r'^country/all/$', ListCountryApiView().as_view(), name='list_country'),
    re_path(r'^country/search/$', ListCountryApiView().as_view(), name='search_country'),

    re_path(r'^region/create/$', CreateRegionApiView().as_view(), name='create_region'),
]