from django.shortcuts import get_object_or_404
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import ShilengaeUser, Country, ShilengaeUserProfile
from api.enums import STATUS


class ShilengaeUserSignupSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), required=False, write_only=True)
    status = serializers.ChoiceField(
        choices=STATUS, write_only=True, required=True)
    type = serializers.ChoiceField(
        choices=ShilengaeUser.ROLE, write_only=True, required=True)

    def custom_signup(self, request, user):
        country = request.data.get('country', None)
        country = get_object_or_404(Country, pk=country)

        user.first_name = self.validated_data.get('first_name')
        user.last_name = self.validated_data.get('last_name')
        user.email = self.validated_data.get('email')
        user.status = self.validated_data.get('status')
        user.type = self.validated_data.get('type')
        user.country = country
        user.save()

    def save(self, request):
        return super(ShilengaeUserSignupSerializer, self).save(request)


class ShilengaeUserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=ShilengaeUser.objects.all(), required=False, write_only=True)

    class Meta:
        model = ShilengaeUserProfile
        fields = ['user', 'mobile_country_code', 'email', 'registration_method',
                  'company_name', 'facebook_id', 'operating_country', 'profile_picture',
                  'online_status', 'business_user', 'verified_mobile', 'verified_email',
                  'verified_phone', 'verified_facebook']
        read_only_fields = ('user',)


class ShilengaeUserSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all())
    country_name = serializers.SerializerMethodField()
    profile = ShilengaeUserProfileSerializer(read_only=True, required=False)
    class Meta:
        model = ShilengaeUser
        fields = ['id', 'first_name', 'email', 'last_name', 'username',
                  'status', 'type', 'last_login', 'country', 'country_name',
                  'profile']

    def get_country_name(self, obj):
        if obj.country:
            return obj.country.name