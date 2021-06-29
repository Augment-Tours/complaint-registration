from rest_framework.serializers import ModelSerializer

from .models import Country

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'currency', 'name', 'symbol', 'timezone', 'status'] 