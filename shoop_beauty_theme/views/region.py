# -*- coding: utf-8 -*-
import json
import os

from django.conf import settings
from django.http import JsonResponse


def region_json(request):
    country = request.GET.get("country")
    # read the local json
    with open(os.path.join(settings.BASE_DIR, "shoop_beauty_theme", "regions.json")) as fp:
        regions = json.load(fp)
    regions = [{"code": r["code"], "name": r["name"]} for r in regions if r["country_code"] == country]
    regions = sorted(regions, key=lambda k: k['name'])
    return JsonResponse(regions, safe=False)
