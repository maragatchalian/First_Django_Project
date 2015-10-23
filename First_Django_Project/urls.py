from django.conf.urls.defaults import patterns, include, url
from First_Django_Project.views import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)
