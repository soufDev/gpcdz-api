from django.db import models
# Create your models here.


class GeoLocation(models.Model):
    socialMedia = models.CharField(null=False, max_length=100)
    dateCreation = models.DateTimeField(null=False, auto_created=True)
    dateUpdate = models.DateTimeField(null=False, auto_now=True)
    createdBy = models.URLField(null=False, max_length=150)
    latitud = models.IntegerField(null=False)
    longitud = models.IntegerField(null=False)
    description = models.TextField()
    type = models.TextField()


class User(models.Model):

    def __init__(self):
        self.url_token = 'http://docker.default:5999/api/token/'
        self.url_users = 'http://docker.default:5999/api/users/'

    def create(self):
        return

