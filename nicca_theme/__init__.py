from django.conf import settings
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from shoop.apps import AppConfig
from shoop.xtheme import Theme


class NiccaTheme(Theme):
    identifier = __name__
    name = _("Nicca Theme")
    author = "Yuki Miyagi"
    template_dir = "nicca/"

    def get_view(self, view_name):
        from . import views
        return getattr(views, view_name, None)

    def _format_cms_links(self, **query_kwargs):
        if "shoop.simple_cms" not in settings.INSTALLED_APPS:
            return
        from shoop.simple_cms.models import Page
        for page in Page.objects.visible().filter(**query_kwargs):
            yield {"url": "/%s" % page.url, "text": force_text(page)}

    def get_cms_navigation_links(self):
        return self._format_cms_links(visible_in_menu=True)


class NiccaThemeAppConfig(AppConfig):
    name = __name__
    verbose_name = NiccaTheme.name
    label = __name__
    provides = {
        "xtheme": __name__ + ":NiccaTheme",
    }


default_app_config = __name__ + ".NiccaThemeAppConfig"
