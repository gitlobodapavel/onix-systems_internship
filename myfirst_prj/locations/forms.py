from django import forms
from .models import Country, Symbol, City


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ('name', 'description', 'population', 'flag', 'cities_count', 'users')


class SymbolForm(forms.ModelForm):

    class Meta:
        model = Symbol
        fields = ('image',)


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('name', 'county', 'longitude', 'latitude',)
