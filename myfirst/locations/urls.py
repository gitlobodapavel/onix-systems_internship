from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries', views.countries_page, name='countries_page'),
    path('country=<str:argument>', views.country_info, name='country_info'),
    path('city=<str:argument>', views.city_info, name='city_info'),
    path('dropcity=<str:argument>', views.drop_city, name='drop_cty')
]
