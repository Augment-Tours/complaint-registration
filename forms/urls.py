from django.urls import include, path, re_path
from rest_framework import routers
from .views import CreateFormApiView, TestView, CreateCategoryApiView, UpdateCategoryApiView, \
    SearchCategoryApiView, CreateFormApiView, UpdateFormApiView

urlpatterns = [
    re_path(r'^test/$', TestView.as_view(), name='test'),
    re_path(r'^category/create/$', CreateCategoryApiView.as_view(),
            name='category_create'),
    re_path(r'^category/update/(?P<pk>\d+)/$',
            UpdateCategoryApiView.as_view(), name='category_update'),
    re_path(r'^category/search/$', SearchCategoryApiView().as_view(),
            name='category_search'),
    re_path(r'^form/create/$', CreateFormApiView.as_view(),
            name='form_create'),
    re_path(r'^form/update/(?P<pk>\d+)/$',
            UpdateFormApiView.as_view(), name='form_update'),
]
