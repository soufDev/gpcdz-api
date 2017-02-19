from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from geolocation.models import GeoLocation
from geolocation.serializers import GeoLocationSerializer


class JSONResponse(HttpResponse):
    """
    HttpResponse qui nous permetera d'avoir nos objet en JSON
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def geolocation_list(request):
    """
    La liste de tout nos objets
    :return:
    """
    if request.method == 'GET':
        geolocation_list = GeoLocation.objects.all()
        serializer = GeoLocationSerializer(geolocation_list, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GeoLocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


def geolocation_detail(request, id):
    """
    recuperé, mettre a jour ou bien supprimer un objet
    :param id:
    :return:
    """

    try:
        geolocation = GeoLocation.objects.get(id=id)
    except GeoLocation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GeoLocationSerializer(geolocation)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GeoLocationSerializer(geolocation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)

        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        geolocation.delete()
        return HttpResponse(status=204)
