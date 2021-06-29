from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Region, City, Country
from .serializers import CountrySerializer

class CreateCountryApiView(generics.CreateAPIView):
    serializer_class = CountrySerializer