from rest_framework import serializers

from geographique_location.models import GeoLocation


class GeoLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocation
        fields = ('socialMedia', 'dateCreation', 'dateUpdate',
                  'userName_createdBy', 'latitud', 'longitud',
                  'description', 'type')


