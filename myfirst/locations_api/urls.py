from django.urls import path
from .views import UsersView, CountryView, SingleCountryView, CityView, CityFilteredView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cities', CityView, basename='user')
router.register(r'cities/country_id/(?P<county>[0-9]+)', CityFilteredView, basename='citiesfiltered')


urlpatterns = [
    path('users/', UsersView.as_view(), name='UserView'),
    path('countries/', CountryView.as_view(), name='UserView'),
    path('countries/<int:pk>', SingleCountryView.as_view(), name='UserView'),
] + router.urls