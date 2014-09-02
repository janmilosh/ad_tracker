from django.conf.urls import include, patterns, url

urlpatterns = patterns('ads.views',
    url(r'^(?P<ad_id>\d+)/$', 'ad'),
    url(r'archive/$', 'archive_ads'),
    url(r'^create/$', 'create'),
)