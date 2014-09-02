from django.conf.urls import include, patterns, url

urlpatterns = patterns('newspapers.views',
    url(r'^(?P<newspaper_id>\d+)/$', 'newspaper'),
    url(r'^create/$', 'create'),
    url(r'^edit/(?P<newspaper_id>\d+)/$', 'edit'),
)