from datetime import datetime

from django.db import models
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
