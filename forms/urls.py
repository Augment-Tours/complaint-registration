from django.urls import include, path, re_path
from rest_framework import routers
from .views import TestView, CreateCategoryApiView, UpdateCategoryApiView, SearchCategoryApiView

urlpatterns = [
    re_path(r'^test/$', TestView.as_view(), name='test'),
    re_path(r'^category/create/$', CreateCategoryApiView.as_view(), name='category_create'),
    re_path(r'^category/update/(?P<pk>\d+)/$', UpdateCategoryApiView.as_view(), name='category_update'),
    re_path(r'^region/search/$', SearchCategoryApiView().as_view(), name='category_search'),

]