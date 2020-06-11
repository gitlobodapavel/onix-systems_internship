from rest_framework import serializers
from rest_framework.response import Response
from django.db import models

from locations.models import Country, City
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()
    email = serializers.CharField()


class CustomUserSerializer(serializers.RelatedField):

    def to_representation(self, value):
        users = User.objects.get(pk=value.pk)
        return {'name': users.username, 'id': value.pk, 'email': users.email, 'last_login': users.last_login}


class CountrySerializer(serializers.ModelSerializer):

    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ('name',
                  'description',
                  'population',
                  'cities_count',
                  'users')


class CustomCountrySerializer(serializers.Serializer):

    def to_representation(self, value):
        countries = Country.objects.get(pk=value.pk)
        return {'name': countries.name, 'description': countries.description, 'population': countries.population}


class CitySerializer(serializers.ModelSerializer):

    county = CustomCountrySerializer()

    class Meta:
        model = City
        fields = (
            'name',
            'longitude',
            'latitude',
            'county'
        )


