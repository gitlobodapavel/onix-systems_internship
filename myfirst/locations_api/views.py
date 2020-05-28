from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from django.contrib.auth.models import User
from locations.models import Country, City

from .serializers import UserSerializer, CountrySerializer, CitySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



class UsersView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})


class CountryView(ListCreateAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SingleCountryView(RetrieveUpdateDestroyAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityView(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityFilteredView(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer

    def list(self, request, *args, **kwargs):

        objects = self.queryset.filter(county=self.kwargs['county'])
        serializer = CitySerializer(objects, many=True)
        return Response(serializer.data)

