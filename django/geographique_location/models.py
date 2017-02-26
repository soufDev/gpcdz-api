from time import time

from django.db import models

import requests
# Create your models here.


class GeoLocation(models.Model):
    socialMedia = models.CharField(null=False, max_length=100)
    dateCreation = models.DateTimeField(auto_now_add=True)
    dateUpdate = models.DateTimeField(auto_now=True)
    userName_createdBy = models.CharField(null=False, max_length=50)
    latitud = models.IntegerField(null=False)
    longitud = models.IntegerField(null=False)
    description = models.TextField()
    type = models.TextField()


class CreatedBy(object):
    url_token = 'http://userservice:5999/api/token'
    url_user = 'http://userservice:5999/api/users/'

    def __init__(self, username='', email='', first_name='', last_name=''):
        self.username = username
        self.email = email
        self.firstName = first_name
        self.lastName = last_name

    def values_key(self, key, dict_array):
        value_key_list = list()
        for dico in dict_array:
            value_key_list.append(dico[key])
        return value_key_list

    def time_limit(self, old_time):
        difference = time() - old_time
        sill = 10.0 * 3600
        return difference > sill

    def get_token(self):
        return requests.get(self.url_token).json()['token']

    def get_timestamp(self):
        return requests.get(self.url_token).json()['timestamp']

    def get_headers(self):
        timestamp_url = self.get_timestamp()
        token = self.get_token()

        if self.time_limit(timestamp_url):
            token = self.get_token()

        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        return headers

    def all(self):
        return requests.get(self.url_user, headers=self.get_headers()).json()

    def get(self, id):
        print(id)
        return requests.get(self.url_user+str(id)+'/', headers=self.get_headers())

    def delete(self, id):
        response = requests.get(self.url_user + str(id) + '/', headers=self.get_headers())
        return response.status_code

    def put(self, id, data):
        return requests.put(self.url_user + str(id) + '/',
                                headers=self.get_headers(),
                                data=data)

    def create(self, data):
        return requests.post(self.url_user, headers=self.get_headers(), data=data)
