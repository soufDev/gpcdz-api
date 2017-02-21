from datetime import datetime, timedelta

from django.test import TestCase

# Create your tests here.
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

