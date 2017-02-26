
from rest_framework import serializers

from geographique_location.models import GeoLocation, CreatedBy


class GeoLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoLocation
        fields = ('socialMedia', 'dateCreation', 'dateUpdate',
                  'userName_createdBy', 'latitud', 'longitud',
                  'description', 'type')


class CreatedBySerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)

    def create(self, validated_data):
        print(validated_data)
        return CreatedBy().create(validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.save()
        return instance
