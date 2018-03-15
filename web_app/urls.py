"""
chopen URL Configuration
"""
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from rest_framework.documentation import include_docs_urls
import sys
# from ion_channel.views import index
from .views import index

# TODO: Check for conflicts in two accounts url pattern
# login_required() from 'django.contrib.auth.urls' redirects to accounts/login/ by default!

urlpatterns = [
    url(r'^docs/', include_docs_urls(title='API Docs')),
    path('viz/', include('viz.urls')),
    # url(r'^cms/', include(wagtailadmin_urls)),
    # url(r'^documents/', include(wagtaildocs_urls)),
    # url(r'^pages/', include(wagtail_urls)),
    # url(r'^accounts/', auth_views.login, name='login', kwargs={'redirect_authenticated_user': True}),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include(('account.urls', 'account'), namespace='account')),
    url(r'^admin/', admin.site.urls),
    url(r'^digitizer/', include(('digitizer.urls', 'digitizer'), namespace="digitizer")),
    url(r'^ion_channel/', include(('ion_channel.urls', 'ion_channel'), namespace="ion_channel")),
    url(r'^channelworm/', include(('channelworm.urls', 'channelworm'), namespace="channelworm")),
    url(r'^api/', include(('api.urls', 'api'), namespace="api")),
    url(r'^index$', index ),
    url(r'^index.html$', index ),
    url(r'^$', index ,name='home'),
    # url(r'^$', include(('homepage.urls', 'homepage'), namespace='homepage')),
    # url(r'^explorer/', include('explorer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

