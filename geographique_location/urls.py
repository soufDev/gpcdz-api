from django.conf.urls import url

from geographique_location import views

urlpatterns = [
    url(r'^users/$', views.get_all_uses, name='all users'),
    url(r'^geolocation/$', views.Geolocation_List.as_view(), name='geolocation_list'),
    url(r'^geolocation/(?P<id>[0-9]+)/$', views.Geolocation_Detail.as_view(), name='geolocation_detail')
]