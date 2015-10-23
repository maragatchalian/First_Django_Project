from django.conf.urls.defaults import patterns, include, url
from First_Django_Project.views import current_datetime#, hours_ahead, hello,
#from First_Django_Project.sample_template import sample_template

urlpatterns = patterns('',
    #url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    #url(r'^sample_template/$', sample_template),
    #url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
