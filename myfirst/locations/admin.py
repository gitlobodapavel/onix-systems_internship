from django.contrib import admin
from django.contrib import admin
from .models import User, Country, City, Symbol

# Register your models here.

admin.site.register(Symbol)
admin.site.register(User)


class CountryAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_filter = ['county']


admin.site.register(City, CityAdmin)

