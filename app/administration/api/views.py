from django.shortcuts import get_object_or_404
from rest_framework import generics, status,viewsets
from rest_framework.response import Response

from administration.models import Country,City,District,County,Address
from .serializers import CountrySerializer,CitySerializer,DistrictSerializer,CountySerializer,AddressSerializer


class CountryListView(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()



class CityListView(generics.ListAPIView):
    serializer_class=CitySerializer
    queryset = City.objects.all()

    def list(self,request,*args,**kwargs):
        country_id = self.kwargs['id']
        print(country_id)
        country=get_object_or_404(Country,id=country_id)
        cities = City.objects.filter(country_id=country.id)
        serializer = CitySerializer(cities,many=True)
        print(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CountyListView(generics.ListAPIView):
    serializer_class = CountySerializer
    queryset = County.objects.all()

    def list(self, request, *args, **kwargs):
        city_id = self.kwargs['id']
        print(city_id)
        city = get_object_or_404(City, id=city_id)
        counties = County.objects.filter(city_id=city.id)
        serializer = CountySerializer(counties, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer