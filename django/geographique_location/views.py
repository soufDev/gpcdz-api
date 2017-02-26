
from django.http.response import Http404

from geographique_location.models import GeoLocation, CreatedBy
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from geographique_location.serializers import GeoLocationSerializer


class UserList(APIView):
    def get(self, request, format=None):
        print(CreatedBy().values_key('username', CreatedBy().all()))
        return Response(
            CreatedBy().all()
        )

    def post(self, request, format=None):
        createdby = CreatedBy().create(request.data)
        if createdby.status_code == 201:
            return Response(createdby.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, id):
        createdby = CreatedBy().get(id)
        if createdby != 200:
            raise Http404
        return createdby

    def get(self, request, id, format=None):
        createdby = CreatedBy().get(id)
        if createdby.status_code == 200:
            return Response(createdby.json(), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        createdby = CreatedBy().put(id, request.data)
        if createdby.status_code == 200:
            return Response(createdby.json(), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        response = CreatedBy().delete(id)
        if response == 204:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
        if request.data['username'] in CreatedBy().values_key('username', CreatedBy().all()):
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Geolocation_Detail(APIView):
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
        serializer = GeoLocationSerializer(geolocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        geolocation = self.get_object(id)
        geolocation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




