from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('countries', views.countries_page, name='countries_page'),
    path('country=<str:argument>', views.country_info, name='country_info'),
    path('city=<str:argument>', views.city_info, name='city_info'),
    path('dropcity=<str:argument>', views.drop_city, name='drop_cty'),
    path('newsymbol', views.new_symbol, name='new_symbol'),
    path('newcountry', views.new_country, name='new_country'),
    path('newcity', views.new_city, name='new_city'),
    path('editcountry_id=<int:country_id>', views.edit_country, name='edit_country'),
    path('editcity_id=<int:city_id>', views.edit_city, name='edit_city'),
]
