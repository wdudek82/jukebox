from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>\d+)/$', views.SnippetDetail.as_view()),

    # Endpoints
    url(r'^playlist/', include('playlist.api.urls'))

]

urlpatterns = format_suffix_patterns(urlpatterns)