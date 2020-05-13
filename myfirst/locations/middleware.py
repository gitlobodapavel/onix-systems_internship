from django.utils.deprecation import MiddlewareMixin
from .models import Country


class GetCounrtiesList(MiddlewareMixin):

    def process_request(self, request):
        countries_list = Country.objects.all()
        request.countries_list = countries_list
        print('[ Log ]: Middleware: ' + str(request.countries_list) + ' have been added to request')
        return None
