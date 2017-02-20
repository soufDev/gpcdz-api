from time import time

from rest_framework import serializers

from geolocation.models import GeoLocation
import requests


class GeoLocationSerializer(serializers.ModelSerializer):
    token_url = 'http://docker.default:5999/api/token'
    createdBy = UserApiSerializer(read_only=True)

    class Meta:
        model = GeoLocation
        fields = ('token_url', 'socialMedia', 'dateCreation', 'dateUpdate',
                  'createdBy', 'latitud', 'longitud', 'description',
                  'type')


class UserApiSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=150)
    userName = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    firstName = serializers.CharField(max_length=100)
    lastName = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return

    def update(self, instance, validated_data):
        return
