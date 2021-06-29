from rest_framework.serializers import ModelSerializer

from .models import Country, Region

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'currency', 'name', 'symbol', 'timezone', 'status']
    
class RegionSerializer(ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = Region
        fields = ['id', 'name', 'symbol', 'country', 'status']
    
    def create(self, validated_data):
        region = super().create(validated_data)
        region.country = validated_data.get('country')
        region.save()

        return region