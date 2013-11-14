from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'web.views.index', name='index'),
    url(r'^([A-Za-z0-9]{1,8})$', 'web.views.resolver', name='resolver'),

    url(r'^admin/', include(admin.site.urls)),
)
