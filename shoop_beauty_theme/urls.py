from django.conf.urls import patterns, url

from shoop_beauty_theme.views import region_json

urlpatterns = patterns(
    '',
    url(r'^region-json/', region_json),
)
