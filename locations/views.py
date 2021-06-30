from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Region, City, Country
from .serializers import CountrySerializer, RegionSerializer

class CreateCountryApiView(generics.CreateAPIView):
    serializer_class = CountrySerializer

class CreateRegionApiView(generics.GenericAPIView):
    serializer_class = RegionSerializer

    def post(self, request, *args, **kwargs):
        country_id = request.data.get('country_id')
        country = get_object_or_404(Country, pk=country_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(country=country)

        return Response(serializer.data, status=status.HTTP_201_CREATED)        

class EditCountryApiView(generics.GenericAPIView):
    serializer_class = CountrySerializer

    def post(self, request, *args, **kwargs):
        country_id = request.data.get("country_id")
        country = get_object_or_404(Country, pk=country_id)

        serializer = self.get_serializer(country, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class EditRegionApiView(generics.GenericAPIView):
    serializer_class = RegionSerializer

    def post(self, request, *args, **kwargs):
        region_id = request.data.get("region_id")
        region = get_object_or_404(Region, pk=region_id)
        
        country_id = request.data.get('country_id')

        
        serializer = self.get_serializer(region, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if country_id:
            country = get_object_or_404(Country, pk=country_id)
            serializer.save(country=country)
        else:
            serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class ListCountryApiView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class ListRegionApiView(generics.ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class SearchCountryApiView(generics.GenericAPIView):
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get('search_term')
        return Country.objects.filter(Q(name__icontains=search_term, 
                                        symbol__icontains=search_term))