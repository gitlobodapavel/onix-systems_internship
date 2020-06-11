from django.core.management.base import BaseCommand
from locations.models import Country
import re


class Command(BaseCommand):
    help = 'Use this cmd to search country by name'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help=u'Name to search')

    def handle(self, *args, **kwargs):

        countries = Country.objects.all()

        for country in countries:
            if re.search(kwargs['name'], country.name):
                print(country.name)