from django.http import HttpResponse
from django.template.loader import render_to_string


def basket_partial(request):
    return HttpResponse(
        render_to_string(
            "nicca/navigation_basket_partial.jinja",
            request=request,
        )
    )
