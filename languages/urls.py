from django.urls import include, path, re_path
from rest_framework import routers
from .views import CreateTranslationPackApiView, ListAllTranslationPacks

urlpatterns = [
    re_path(r'^translation_pack/create/$', CreateTranslationPackApiView().as_view(), name='create_translation_pack'),
    re_path(r'^translation_pack/all/$', ListAllTranslationPacks().as_view(), name='list_translation_pack'),
]