from django.shortcuts import get_object_or_404
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import ShilengaeUser, Country
from api.enums import STATUS
from locations.serializers import CountrySerializer

class ShilengaeUserSignupSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), required=True, write_only=True)
    status = serializers.ChoiceField(choices=STATUS, write_only=True, required=True)

    def custom_signup(self, request, user):
        country = request.data.get('country', None)
        country = get_object_or_404(Country, pk=country)

        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.status = self.validated_data.get('status')
        user.country = country
        user.save()

    def save(self, request):
        return super(ShilengaeUserSignupSerializer, self).save(request)

class ShilengaeUserSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    class Meta:
        model = ShilengaeUser
        fields = ['id', 'first_name', 'last_name', 'status', 'last_login', 'country']