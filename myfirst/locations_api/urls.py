from django.urls import path
from .views import UsersView, CountryView, SingleCountryView, CityView, CityFilteredView, GoogleView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .doc_yasg import urlpatterns as doc_urls

router = DefaultRouter()
router.register(r'cities', CityView, basename='user')
router.register(r'cities/country_id/(?P<county>[0-9]+)', CityFilteredView, basename='citiesfiltered')


urlpatterns = [
    path('users/', UsersView.as_view(), name='UserView'),
    path('countries/', CountryView.as_view(), name='UserView'),
    path('countries/<int:pk>', SingleCountryView.as_view(), name='UserView'),
    path('google/', GoogleView.as_view(), name='google'),

    # JWT auth urls

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

urlpatterns += doc_urls
