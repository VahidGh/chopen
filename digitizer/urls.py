from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^cvs_export/$', csv_export, name='csv_export'),
    url(r'^(?P<graph_id>[0-9]+)$', digitize, name='digitize'),
]