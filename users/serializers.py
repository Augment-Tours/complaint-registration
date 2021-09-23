from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework import serializers

from .models import CRUser
from api.enums import STATUS

class CRUserSignupSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    type = serializers.ChoiceField(
        choices=CRUser.TYPE, write_only=True, required=True)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.email = self.validated_data.get('email')
        user.type = self.validated_data.get('type')
        user.save()

    def save(self, request):
        return super(CRUserSignupSerializer, self).save(request)

class CRUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CRUser
        fields = ('id', 'first_name', 'last_name', 'email', 'type', 'status')
        