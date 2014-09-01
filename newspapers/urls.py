from django.conf.urls import include, patterns, url

urlpatterns = patterns('newspapers.views',
    url(r'^(?P<newspaper_id>\d+)/$', 'newspaper'),
)