from django.db import models
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .tasks import send_email
from django.shortcuts import get_object_or_404

# Create your models here.


class Symbol(models.Model):
    image = models.ImageField(null=False, blank=False)


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True)
    population = models.IntegerField(default=0)
    flag = models.OneToOneField(Symbol, on_delete=models.CASCADE)
    cities_count = models.IntegerField(default=0)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    county = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="county")
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=City)
def pre_save_city(sender, **kwargs):
    print("[ Log ]: New city will be added to database")


@receiver(post_save, sender=City)
def post_save_country(instance, **kwargs):
    instance.county.cities_count += 1
    instance.county.save()


@receiver(pre_delete, sender=City)
def pre_delete_country(instance, **kwargs):
    instance.county.cities_count -= 1
    instance.county.save()


@receiver(post_delete, sender=City)
def post_delete_city(sender, **kwargs):
    print("[ Log ]: One city have been removed from database")


@receiver(post_save, sender=Country)
def post_save_country(instance, created, **kwargs):
    if created: # if country was created
        message = "New country " + str(instance.name) + " created successfully !"
        send_email.delay(message)
    else: # if country was edited
        country = get_object_or_404(Country, name=instance.name)
        print(instance.users)
        message = "Country " + str(instance.name) + " edited successfully ! Link: http://127.0.0.1:8000/locations/country/" + str(country.id)
        send_email.delay(message)
