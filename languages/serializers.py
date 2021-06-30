from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import TranslationPack

class TranslationPackSerializer(ModelSerializer):
    class Meta:
        model = TranslationPack
        fields = ['version', 'name', 'translation_file']