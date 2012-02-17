from django.conf.urls.defaults import patterns, include, url
from views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^hello/(?P<lang>\w{2})/$', hello),
                       url(r'^$', hello),
)
