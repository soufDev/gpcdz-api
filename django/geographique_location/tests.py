
from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.test.client import RequestFactory
from rest_framework import status

from geographique_location.models import GeoLocation


class GeoLocationTest(TestCase):

    def test_created_at_present(self):
        """
        test if the created_at is on the futur or in the present
        :return:
        """
        GeoLocation.objects.create(
            socialMedia='whatsup',
            userName_createdBy='soufDev',
            latitud=848451841,
            longitud=5145151545,
            description='iohiouhiu',
            type='type')
        GeoLocation.objects.create(
            socialMedia='facebook',
            userName_createdBy='imad',
            latitud=848451841,
            longitud=5145151545,
            description='iohiouhiu',
            type='type')

        saved_items = GeoLocation.objects.all()
        self.assertEquals(saved_items.count(), 2)

        first_item = saved_items[0]
        second_item = saved_items[1]

        self.assertEquals(first_item.socialMedia, 'whatsup')
        self.assertEquals(first_item.userName_createdBy, 'soufDev')
        self.assertNotEquals(first_item.dateCreation, None)
        self.assertNotEquals(first_item.dateUpdate, None)

        self.assertEquals(second_item.socialMedia, 'facebook')
        self.assertEquals(second_item.userName_createdBy, 'imad')
        self.assertNotEquals(first_item.dateCreation, None)
        self.assertNotEquals(first_item.dateUpdate, None)


class GeoLocationListTest(TestCase):
    def setUp(self):
        self.obj1 = GeoLocation.objects.create(
            socialMedia='whatsup',
            userName_createdBy='soufDev',
            latitud=848451841,
            longitud=5145151545,
            description='iohiouhiu',
            type='type')
        self.obj2 = GeoLocation.objects.create(
            socialMedia='facebook',
            userName_createdBy='imad',
            latitud=848451841,
            longitud=5145151545,
            description='iohiouhiu',
            type='type')

    def test_url_resolve(self):
        response = self.client.get('/geolocations/', follow=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

        request = self.client.post('/geolocations/', {
            'socialMedia': 'snapchat',
            'userName_createdBy': 'soufiane',
            'latitud': 848451841,
            'longitud': 5145151545,
            'description': 'iohiouhiu',
            'type': 'type'
        })
        self.assertEquals(request.status_code, status.HTTP_201_CREATED)


class GeoLocationDetailTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.user = User.objects.create_superuser(username='soufiane', email='soufiane@example.com', password='123456')
        self.obj1 = GeoLocation.objects.create(
            socialMedia='whatsup',
            userName_createdBy='soufDev',
            latitud=848451841,
            longitud=5145151545,
            description='iohiouhiu',
            type='type')
        self.obj2 = GeoLocation.objects.create(
            socialMedia='facebook',
            userName_createdBy='imad',
            latitud=848451841,
            longitud=5145151545,
            description='iohiouhiu',
            type='type')

    def test_url_resolve(self):

        response = self.client.get('/geolocation/'+str(self.obj1.id)+'/')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        data = {
            "socialMedia": "snapchat",
            "userName_createdBy": "soufiane",
            "latitud": 848451841,
            "longitud": 5145151545,
            "description": "iohiouhiu",
            "type": "type"
        }
        content_type = 'application/json'
        response = self.client.put('/geolocation/'+str(self.obj1.id)+'/', data, content_type)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        response = self.client.delete('/geolocation/'+str(self.obj1.id)+'/', content_type=content_type)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
