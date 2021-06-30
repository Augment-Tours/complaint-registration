from django.urls import include, path, re_path
from rest_framework import routers
from .views import CreateCountryApiView, CreateRegionApiView, CreateCityApiView, \
                    EditCountryApiView, EditRegionApiView, EditCityApiView, \
                    ListCountryApiView, ListRegionApiView, \
                    SearchCountryApiView, SearchRegionApiView

urlpatterns = [
    re_path(r'^country/create/$', CreateCountryApiView().as_view(), name='create_country'),
    re_path(r'^country/edit/$', EditCountryApiView().as_view(), name='edit_country'),
    re_path(r'^country/all/$', ListCountryApiView().as_view(), name='list_country'),
    re_path(r'^country/search/$', SearchCountryApiView().as_view(), name='search_country'),

    re_path(r'^region/create/$', CreateRegionApiView().as_view(), name='create_region'),
    re_path(r'^region/edit/$', EditRegionApiView().as_view(), name='edit_region'),
    re_path(r'^region/all/$', ListRegionApiView().as_view(), name='list_region'),
    re_path(r'^region/search/$', SearchRegionApiView().as_view(), name='search_region'),
    
    re_path(r'^city/create/$', CreateCityApiView().as_view(), name='create_city'),
    re_path(r'^city/edit/$', EditCityApiView().as_view(), name='edit_city'),
]