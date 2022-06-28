from django.conf.urls import patterns, re_path

from shoop_beauty_theme.views import region_json

urlpatterns = patterns(
    "",
    re_path(r"^region-json/", region_json),
)
