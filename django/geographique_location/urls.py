from django.conf.urls import url

from geographique_location import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='all_users'),
    url(r'^users/(?P<id>([a-zA-Z0-9]+))/$', views.UserDetail.as_view(), name='user_detail'),
    url(r'^geolocations/$', views.Geolocation_List.as_view(), name='geolocation_list'),
    url(r'^geolocation/(?P<id>[0-9]+)/$', views.Geolocation_Detail.as_view(), name='geolocation_detail')
]