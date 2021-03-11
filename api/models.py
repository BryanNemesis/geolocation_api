from django.db import models


class GeoData(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    continent_name = models.CharField(max_length=20)
    country_name = models.CharField(max_length=200)
    region_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
