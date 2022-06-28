from django import forms
from shoop.front.template_helpers.general import (
    get_newest_products,
    get_best_selling_products,
    get_random_products,
)
from shoop.xtheme.plugins._base import TemplatedPlugin  # TODO: FIX THIS.
from django.utils.translation import gettext_lazy as _


class ProductHighlightPlugin(TemplatedPlugin):
    identifier = "shoop_beauty_theme.product_highlight"
    name = _("Shoop Beauty Theme Product Highlights")
    template_name = "shoop_beauty_theme/highlight_plugin.jinja"
    fields = [
        ("title", forms.CharField(required=False, initial="")),
        (
            "type",
            forms.ChoiceField(
                choices=[
                    ("newest", "Newest"),
                    ("best_selling", "Best Selling"),
                    ("random", "Random"),
                ],
                initial="newest",
            ),
        ),
        ("count", forms.IntegerField(min_value=1, initial=8)),
    ]

    def get_context_data(self, context):
        type = self.config.get("type", "newest")
        count = self.config.get("count", 8)
        if type == "newest":
            products = get_newest_products(context, count)
        elif type == "best_selling":
            products = get_best_selling_products(context, count)
        elif type == "random":
            products = get_random_products(context, count)
        else:
            products = []

        return {
            "request": context["request"],
            "title": self.config.get("title"),
            "products": products,
        }
