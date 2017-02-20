from django.http.response import Http404

# Create your views here.
from rest_framework import generics, status

from rest_framework.response import Response
from rest_framework.views import APIView

from geolocation.models import GeoLocation
from geolocation.serializers import GeoLocationSerializer


from time import time
import requests


class GeolocationList(generics.ListCreateAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class GeolocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer


class Geolocation_List(APIView):
    """
    La liste de tout nos objets
    :return:
    """
    def get(self, request, format=None):
        geolocations = GeoLocation.objects.all()
        serializer = GeoLocationSerializer(geolocations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeoLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Geolocation_Detail(APIView):
    url_token = 'http://docker.default:5999/api/token'

    def get_object(self, id):
        try:
            return GeoLocation.objects.get(pk=id)
        except GeoLocation.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        geolocation = self.get_object(id)
        serializer = GeoLocationSerializer(geolocation)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        geolocation = self.get_object(id)
        serializer = GeoLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        geolocation = self.get_object(id)
        geolocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def time_limit(old_time):
    difference = time() - old_time
    sill = 10.0 * 3600
    return difference > sill


def get_token(url):
    return requests.get(url).json()['token']


def get_timestamp(url):
    return requests.get(url).json()['timestamp']


def get_headers(url_token):
    timestamp_url = get_timestamp(url_token)
    token = get_token(url_token)

    if time_limit(timestamp_url):
        token = get_token(url_token)

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }
    return headers


def get_all_uses(url_token, url_user):
    return requests.get(url_user, headers=get_headers(url_token)).json()


def user_get(url_token, url_user):
    return requests.get(url_user, headers=get_headers(url_token)).json()


def user_delete(url_token, url_user):
    return requests.delete(url_user, headers=get_headers(url_token))


def user_put(url_token, url_user):
    return requests.put(url_user, headers=get_headers(url_token))


def user_post(url_token, url_user):
    return requests.post(url_user, headers=get_headers(url_token))


