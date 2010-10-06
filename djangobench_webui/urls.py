import os
from django.conf import settings
from django.conf.urls.defaults import *
from djangobench_webui import webui


urlpatterns = patterns('',
    (r'', include('djangobench_webui.webui.urls')),
)

if settings.DEBUG:
    document_root = os.path.join(os.path.dirname(webui.__file__), 'media')
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': document_root}),
    )
