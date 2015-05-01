from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', include('schoolapp.urls')),
    url(r'^school/', include('schoolapp.urls', namespace='school')),
    url(r'^admin/', include(admin.site.urls)),
)
