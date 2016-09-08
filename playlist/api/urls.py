from django.conf.urls import url
from playlist.api import views


urlpatterns = [
    url(r'^album/$', views.AlbumList.as_view()),
    url(r'^album/(?P<pk>\d+)/$', views.AlbumDetail.as_view()),

    url(r'^artist/$', views.ArtistList.as_view()),
    url(r'^artist/(?P<pk>\d+)/$', views.ArtistDetail.as_view()),

    url(r'^soundcode/$', views.SoundcodeList.as_view()),
    url(r'^soundcode/(?P<pk>\d+)/$', views.SoundcodeDetail.as_view()),

    url(r'^song/$', views.SongList.as_view()),
    url(r'^song/(?P<pk>\d+)/$', views.SongDetail.as_view()),
]