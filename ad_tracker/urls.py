from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'ad_tracker.views.login'),
    url(r'^accounts/auth/$', 'ad_tracker.views.auth_view'),
    url(r'^accounts/logout/$', 'ad_tracker.views.logout'),
    url(r'^accounts/loggedin/$', 'ad_tracker.views.loggedin'),
    url(r'^accounts/invalid/$', 'ad_tracker.views.invalid_login'),
    url(r'^$', 'ad_tracker.views.home', name='home'),
    url(r'^newspaper/', include('newspapers.urls')),
    url(r'^ad/', include('ads.urls')),
)
