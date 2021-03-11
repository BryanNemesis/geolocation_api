from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import GeoData


class GeoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoData
        fields = [
            'ip',
            'continent_name',
            'country_name',
            'region_name',
            'city',
            'latitude',
            'longitude',
        ]
