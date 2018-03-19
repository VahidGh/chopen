from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.documentation import include_docs_urls
from .views import *


urlpatterns = [
    # url(r'^', index, name='index'),
    # url(r'^docs/', include_docs_urls(title='API Docs')),
    # url(r'^docs/', include_docs_urls(title='API Docs', public=False)),
    # url(r'^', include_docs_urls(title='API Docs', public=False)),

    url(r'^channelworm_gene/create/$', login_required(ChannelwormGeneCreateAPI.as_view()), name="channelworm-gene-create-api"),
    url(r'^channelworm_gene/list/$', ChannelwormGeneListAPI.as_view(), name="channelworm-gene-list-api"),
    url(r'^channelworm_gene/details/(?P<pk>[0-9]+)/$', ChannelwormGeneDetailsAPI.as_view(), name="channelworm-gene-details-api"),

    url(r'^channelworm_protein/create/$', login_required(ChannelwormProteinCreateAPI.as_view()), name="channelworm-protein-create-api"),
    url(r'^channelworm_protein/list/$', ChannelwormProteinListAPI.as_view(), name="channelworm-protein-list-api"),
    url(r'^channelworm_protein/details/(?P<pk>[0-9]+)/$', ChannelwormProteinDetailsAPI.as_view(), name="channelworm-protein-details-api"),

    url(r'^ion_channel/create/$', login_required(IonChannelCreateAPI.as_view()), name="ion-channel-create-api"),
    url(r'^ion_channel/list/$', IonChannelListAPI.as_view(), name="ion-channel-list-api"),
    url(r'^ion_channel/details/(?P<pk>[0-9]+)/$', IonChannelDetailsAPI.as_view(), name="ion-channel-details-api"),

    url(r'^reference/create/$', login_required(ReferenceCreateAPI.as_view()), name="reference-create-api"),
    url(r'^reference/list/$', ReferenceListAPI.as_view(), name="reference-list-api"),
    url(r'^reference/details/(?P<pk>[0-9]+)/$', ReferenceDetailsAPI.as_view(), name="reference-details-api"),

    url(r'^cell/create/$', login_required(CellCreateAPI.as_view()), name="cell-create-api"),
    url(r'^cell/list/$', CellListAPI.as_view(), name="cell-list-api"),
    url(r'^cell/details/(?P<pk>[0-9]+)/$', CellDetailsAPI.as_view(), name="cell-details-api"),

    url(r'^patch_clamp/create/$', login_required(PatchClampCreateAPI.as_view()), name="patch-clamp-create-api"),
    url(r'^patch_clamp/list/$', PatchClampListAPI.as_view(), name="patch-clamp-list-api"),
    url(r'^patch_clamp/details/(?P<pk>[0-9]+)/$', PatchClampDetailsAPI.as_view(), name="patch-clamp-details-api"),

    url(r'^graph/create/$', login_required(GraphCreateAPI.as_view()), name="graph-create-api"),
    url(r'^graph/list/$', GraphListAPI.as_view(), name="graph-list-api"),
    url(r'^graph/details/(?P<pk>[0-9]+)/$', GraphDetailsAPI.as_view(), name="graph-details-api"),

    url(r'^graph_data/(?P<pk>[0-9]+)$', GraphDataSeriesAPI.as_view(), name='graph-data-index-api'),
    url(r'^graph_data/create/$', login_required(GraphDataCreateAPI.as_view()), name="graph-data-create-api"),
    url(r'^graph_data/list/$', GraphDataListAPI.as_view(), name="graph-data-list-api"),
    url(r'^graph_data/details/(?P<pk>[0-9]+)/$', GraphDataDetailsAPI.as_view(), name="graph-data-details-api"),

    url(r'^user/list/$', UserListAPI.as_view(), name="user-list-api"),
    url(r'^user/details/(?P<pk>[0-9]+)/$', UserDetailsAPI.as_view(), name="user-details-api"),

]

urlpatterns = format_suffix_patterns(urlpatterns)