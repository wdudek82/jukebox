from django.conf.urls import url
from playlist.api import views


urlpatterns = [
    url(r'^album/list/$', views.AlbumList.as_view()),
    url(r'^album/(?P<pk>\d+)/$', views.AlbumList.as_view()),

    url(r'^artist/list/$', views.ArtistList.as_view()),
    url(r'^artist/(?P<pk>\d+)/$', views.ArtistDetail.as_view()),

    url(r'^category/list/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>\d+)/$', views.CategoryDetail.as_view()),

    url(r'^genre/list/$', views.GenreList.as_view()),
    url(r'^genre/(?P<pk>\d+)/$', views.GenreDetail.as_view()),

    url(r'^track/list/$', views.TrackList.as_view()),
    url(r'^track/(?P<pk>\d+)/$', views.TrackDetail.as_view()),
]