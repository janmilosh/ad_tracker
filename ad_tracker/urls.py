from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'ad_tracker.views.login'),
    url(r'^auth/$', 'ad_tracker.views.auth_view'),
    url(r'^logout/$', 'ad_tracker.views.logout'),
    url(r'^loggedin/$', 'ad_tracker.views.loggedin'),
    url(r'^invalid/$', 'ad_tracker.views.invalid_login'),
    url(r'^register/$', 'ad_tracker.views.register_user'),
    url(r'^register_success/$', 'ad_tracker.views.register_success'),
    url(r'^$', 'ad_tracker.views.home', name='home'),
    url(r'^newspaper/', include('newspapers.urls')),
    url(r'^ad/', include('ads.urls')),
)
