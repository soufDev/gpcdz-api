from time import time

from rest_framework import serializers

from geolocation.models import GeoLocation
import requests


def time_limit(old_time):
    difference = time() - old_time
    sill = 10 * 3600
    return difference > sill


def get_token(url):
    return requests.get(url).json()['token']


def get_timestamp(url):
    return requests.get(url).json()['timestamp']


def get_headers(url_token, url_user):
    timestamp_url = get_timestamp(url_token)
    token = get_token(url_token)

    if time_limit(timestamp_url):
        token = get_token(url_token)

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    return headers


def createdby_get(id, url_token, url_user):
    return requests.get(url_user+id, headers=get_headers(url_token, url_user)).json()


def createdby_delete(id, url_token, url_user):
    return requests.delete(url_user+id, headers=get_headers(url_token, url_user))


def createdby_put(id, url_token, url_user):
    return requests.put(url_user+id, headers=get_headers(url_token, url_user))



class GeoLocationSerializer(serializers.ModelSerializer):
    createdBy = serializers.HyperlinkedIdentityField()

    class Meta:
        model = GeoLocation
        fields = ('socialMedia', 'dateCreation', 'dateUpdate',
                  'createdBy', 'latitud', 'longitud', 'description',
                  'type')



