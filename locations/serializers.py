from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Country, Region, City

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'currency', 'name', 'symbol', 'timezone', 'status']
    
class RegionSerializer(ModelSerializer):
    country = CountrySerializer
    country_name = serializers.SerializerMethodField()
    class Meta:
        model = Region
        fields = ['id', 'name', 'symbol', 'country', 'status', 'country_name']
    
    def create(self, validated_data):
        region = super().create(validated_data)
        region.country = validated_data.get('country')
        region.save()

        return region

    def get_country_name(self, obj):
        return obj.country.name

class CitySerializer(ModelSerializer):
    region = RegionSerializer
    region_name = serializers.SerializerMethodField()
    class Meta:
        model = City
        fields = ['id', 'name', 'symbol', 'region', 'status', 'region_name']
    
    def create(self, validated_data):
        city = super().create(validated_data)
        city.region = validated_data.get('region')
        city.save()

        return city

    def get_region_name(self, obj):
        return obj.region.name