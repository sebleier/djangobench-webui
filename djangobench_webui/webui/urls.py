from django.conf.urls.defaults import *


urlpatterns = patterns('djangobench_webui.webui.views',
    (r'^$', 'results'),
    (r'^data/(?P<benchmark>\w+)/$', 'benchmark_data'),
    (r'^data/(?P<benchmark>\w+)/realtime/$', 'benchmark_realtime'),
)
