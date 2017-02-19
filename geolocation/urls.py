from django.conf.urls import url

from geolocation import views

urlpatterns = [
    url(r'^geolocation/$', views.geolocation_list, name='geolocation_list'),
    url(r'^geolocation/(?P<id>[0-9]+)/$', views.geolocation_detail, name='geolocation_detail')
]