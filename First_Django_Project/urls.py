from django.conf.urls.defaults import patterns, include, url
from First_Django_Project.views import hello, current_datetime

urlpatterns = patterns('',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
)
