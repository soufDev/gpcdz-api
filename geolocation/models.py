from django.db import models

# Create your models here.


class GeoLocation(models.Model):
    socialMedia = models.CharField(null=False, max_length=100)
    dateCreation = models.DateTimeField(null=False, auto_created=True)
    dateUpdate = models.DateTimeField(null=False, auto_now=True)
    latitud = models.IntegerField(null=False)
    longitud = models.IntegerField(null=False)
    description = models.TextField()
    type = models.TextField()


