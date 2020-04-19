from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Welcome to localhost:port/locations/")


def get_argument(request, argument):
    return render(request, 'locations/url_arguments.html', context={'argument': argument})
