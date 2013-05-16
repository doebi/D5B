from django.conf.urls import patterns, include, url
from django.shortcuts import redirect

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('event.views',
        url(r'^$', 'index'),
        url(r'^track/(?P<user_id>\w+)/(?P<brand>\w+)/$', 'track'),
        url(r'^deposit/$', 'deposit'),
        url(r'^user/(?P<user_id>\w+)/$', 'user'),
        url(r'^user/$', 'userlist'),
        url(r'^stats/$', 'stats'),
)

