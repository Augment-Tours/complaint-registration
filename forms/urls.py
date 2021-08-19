from django.urls import include, path, re_path
from .views import CreateFormApiView, TestView, CreateCategoryApiView, UpdateCategoryApiView, \
    SearchCategoryApiView, CreateFormApiView, UpdateFormApiView, \
    CreateFormFieldApiView, UpdateFormFieldApiView, SearchFormApiView, ListFormApiView, ListCategoriesApiView, \
    ListFieldsByFormApiView, CategoryDetailApiView, ListFormFieldByCategoryApiView, \
    DeleteFormApiView

urlpatterns = [
    re_path(r'^create/$', CreateFormApiView.as_view(),
            name='form_create'),
    re_path(r'^update/(?P<pk>\d+)/$',
            UpdateFormApiView.as_view(), name='form_update'),
    re_path(r'^search/$', SearchFormApiView().as_view(),
            name='form_search'),
    re_path(r'^all/$', ListFormApiView().as_view(),
            name='form_list'),
    re_path(r'^delete/(?P<pk>\d+)/$', DeleteFormApiView().as_view(),
            name='form_delete'),
    re_path(r'^test/$', TestView.as_view(), name='test'),
    re_path(r'^category/create/$', CreateCategoryApiView.as_view(),
            name='category_create'),
    re_path(r'^category/all/$', ListCategoriesApiView.as_view(),
            name='category_list'),
    re_path(r'^category/update/(?P<pk>\d+)/$',
            UpdateCategoryApiView.as_view(), name='category_update'),
    re_path(r'^category/search/$', SearchCategoryApiView().as_view(),
            name='category_search'),
    re_path(r'^category/detail/(?P<pk>\d+)/$',CategoryDetailApiView.as_view(), 
            name='category_detail'),
    re_path(r'^category/fields/(?P<pk>\d+)/$',ListFormFieldByCategoryApiView.as_view(), 
            name='category_fields'),
    re_path(r'^fields/create/$', CreateFormFieldApiView.as_view(),
            name='form_field_create'),
    re_path(r'^fields/(?P<pk>\d+)/$', ListFieldsByFormApiView.as_view(),
            name='form_field_create'),
    re_path(r'^fields/update/(?P<pk>\d+)/$',
            UpdateFormFieldApiView.as_view(), name='form_field_update'),
]
