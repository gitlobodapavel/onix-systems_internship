from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Country, City
from .forms import CountryForm, SymbolForm, CityForm

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
    return render(request, 'locations/countries.html', {
        'countries_objects': countries_objects,
    })


@login_required(login_url='/login/')
def drop_city(request, argument):
    city = get_object_or_404(City, name=argument)
    country = city.county
    city.delete()
    return redirect('/locations/country='+str(country.name))


@login_required(login_url='/login/')
def new_country(request):

    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save()
            country.save()
            return redirect('/locations/countries')
    else:
        form = CountryForm()

    return render(request, 'locations/newcountry.html', {
        'form': form,
    })


@login_required(login_url='/login/')
def new_symbol(request):

    if request.method == "POST":
        form = SymbolForm(request.POST, request.FILES)
        if form.is_valid():
            symbol = form.save()
            print("[ Log ]: New symbol saved")
            return redirect('/locations/newcountry')
    else:
        form = SymbolForm()
        print("[ Log ]: Open new form for Symbol creation")

    return render(request, 'locations/addsymbol.html', {
        'form': form,
    })


@login_required(login_url='/login/')
def new_city(request):

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            # city.save()
            return redirect('/locations/countries')
        else:
            return HttpResponse("The form is not valid")
    else:
        form = CityForm()
    return render(request, 'locations/newcity.html', {
        'form': form,
    })


@login_required(login_url='/login/')
def edit_country(request, country_id):

    country = get_object_or_404(Country, id=country_id)
    print("[ Log ]: selected country to edit: " + country.name)

    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            country = form.save()
            # country.save()
            return redirect('/locations/countries')
    else:
        form = CountryForm(instance=country)
    return render(request, 'locations/editcountry.html', {
        'form': form,
        'country': country,
    })


@login_required(login_url='/login/')
def edit_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    print("[ Log ]: selected city to edit: " + city.name)

    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            city = form.save()
            country = get_object_or_404(Country, name=city.county)
            country.cities_count = country.cities_count - 1
            country.save()
            # city.save()
            return redirect('/locations/countries')
    else:
        form = CityForm(instance=city)

    return render(request, 'locations/editcity.html', {
        'form': form,
    })