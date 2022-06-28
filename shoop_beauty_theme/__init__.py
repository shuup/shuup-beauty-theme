from django.conf import settings
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _

from shoop.apps import AppConfig
from shoop.xtheme import Theme


class ShoopBeautyTheme(Theme):
    identifier = __name__
    name = _("Shoop Beauty Theme")
    author = "Juha Kujala & Yuki Miyagi"
    template_dir = "shoop_beauty_theme/"

    def get_view(self, view_name):
        from . import views

        return getattr(views, view_name, None)

    def _format_cms_links(self, **query_kwargs):
        if "shoop.simple_cms" not in settings.INSTALLED_APPS:
            return
        from shoop.simple_cms.models import Page

        for page in Page.objects.visible().filter(**query_kwargs):
            yield {"url": "/%s" % page.url, "text": force_str(page)}

    def get_cms_navigation_links(self):
        return self._format_cms_links(visible_in_menu=True)


class ShoopBeautyThemeAppConfig(AppConfig):
    name = __name__
    verbose_name = ShoopBeautyTheme.name
    label = __name__
    provides = {
        "xtheme": __name__ + ":ShoopBeautyTheme",
        "xtheme_plugin": [
            "shoop_beauty_theme.plugins:ProductHighlightPlugin",
        ],
        "front_urls": ["shoop_beauty_theme.urls:urlpatterns"],
    }


default_app_config = __name__ + ".ShoopBeautyThemeAppConfig"
