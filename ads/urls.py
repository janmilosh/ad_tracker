from django.conf.urls import include, patterns, url

urlpatterns = patterns('ads.views',
    url(r'^(?P<ad_id>\d+)/$', 'ad'),
    url(r'archive/$', 'archive_ads'),
    url(r'^create/$', 'create'),
    url(r'^edit/(?P<ad_id>\d+)/$', 'edit'),
    url(r'^confirm_delete/(?P<ad_id>\d+)/$', 'confirm_delete'),
    url(r'^delete/(?P<ad_id>\d+)/$', 'delete'),
)