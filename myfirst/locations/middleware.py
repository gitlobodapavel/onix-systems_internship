from django.utils.deprecation import MiddlewareMixin
from .models import Country


class GetCounrtiesList(MiddlewareMixin):

    def process_request(self, request):
        countries_list = Country.objects.all()
        request.countries_list = countries_list
        return None
