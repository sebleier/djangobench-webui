from django.conf import settings
from django.conf.urls.defaults import *
import os
import webui



urlpatterns = patterns('',
    (r'^$', 'webui.views.results'),
    (r'^data/(?P<benchmark>\w+)', 'webui.views.benchmark_data'),
)

if settings.DEBUG:
    document_root = os.path.join(os.path.dirname(webui.__file__), 'media')
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': document_root}),
    )
