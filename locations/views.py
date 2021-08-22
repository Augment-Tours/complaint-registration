from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import generics, permissions, serializers, status
from rest_framework.response import Response

from .models import Region, City, Country
from .serializers import CountrySerializer, RegionSerializer, CitySerializer

class CreateCountryApiView(generics.CreateAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateRegionApiView(generics.GenericAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        country_id = request.data.get('country_id', None)
        if not country_id:
            raise serializers.ValidationError('Country id is required.')
        country = get_object_or_404(Country, pk=country_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(country=country)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateCityApiView(generics.GenericAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        region_id = request.data.get('region_id')
        region = get_object_or_404(Region, pk=region_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(region=region)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EditCountryApiView(generics.GenericAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        country_id = request.data.get("country_id")
        country = get_object_or_404(Country, pk=country_id)

        serializer = self.get_serializer(country, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class EditRegionApiView(generics.GenericAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

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

class EditCityApiView(generics.GenericAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        city_id = request.data.get("city_id")
        city = get_object_or_404(City, pk=city_id)
        
        region_id = request.data.get('region_id')
        
        serializer = self.get_serializer(city, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if region_id:
            region = get_object_or_404(Region, pk=region_id)
            serializer.save(region=region)
        else:
            serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class ListCountryApiView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ListRegionApiView(generics.ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ListCityApiView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class SearchCountryApiView(generics.ListAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        return Country.objects.filter(Q(name__icontains=search_term) | \
                                        Q(symbol__icontains=search_term))

class SearchRegionApiView(generics.ListAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        return Region.objects.filter(Q(name__icontains=search_term) |
                                        Q(symbol__icontains=search_term))

class SearchCityApiView(generics.ListAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_term = self.request.query_params.get('search_term')
        return City.objects.filter(Q(name__icontains=search_term) |
                                    Q(symbol__icontains=search_term))
class RegionDetailApiView(generics.RetrieveAPIView):
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Region.objects.all()

class CountryDetailApiView(generics.RetrieveAPIView):
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Country.objects.all()

class CityDetailApiView(generics.RetrieveAPIView):
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = City.objects.all()

