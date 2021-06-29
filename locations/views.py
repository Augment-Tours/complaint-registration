from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Region, City, Country
from .serializers import CountrySerializer

class CreateCountryApiView(generics.CreateAPIView):
    serializer_class = CountrySerializer

class EditCountryApiView(generics.GenericAPIView):
    serializer_class = CountrySerializer

    def post(self, request, *args, **kwargs):
        country_id = request.data.get("country_id")
        country = get_object_or_404(Country, pk=country_id)

        serializer = self.get_serializer(country, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)