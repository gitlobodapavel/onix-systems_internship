from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Country, City

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    user = request.user
    return render(request, 'locations/home.html', {'user': user})


@login_required(login_url='/login/')
def country_info(request, argument):
    countries_objects = Country.objects.all()
    name_list = []
    cities_list = []

    for item in countries_objects:
        if item.name == argument:
            cities_list = City.objects.filter(county_id=item.id)

    for item in countries_objects:
        name_list.append(item.name)

    list_len = cities_list.__len__()

    return render(request, 'locations/country.html', context={
        'argument': argument,
        'cities_list': cities_list,
        'name_list': name_list,
        'list_len': list_len
    })


@login_required(login_url='/login/')
def city_info(request, argument):
    city = get_object_or_404(City, name=argument)
    return render(request, 'locations/city.html', context={
        'argument': argument,
        'city': city,
    })


@login_required(login_url='/login/')
def countries_page(request):
    countries_objects = Country.objects.all()
    print(countries_objects)
    return render(request, 'locations/countries.html', {
        'countries_objects': countries_objects,
    })


@login_required(login_url='/login/')
def drop_city(request, argument):
    city = get_object_or_404(City, name=argument)
    country = city.county
    city.delete()
    return redirect('/locations/country='+str(country.name))
