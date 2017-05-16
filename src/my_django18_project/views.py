from django.conf import settings

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics
import json
from .twtwrapper import TWT


@csrf_protect
def twt_search(request):
    keyword = request.GET["q"]
    items = TWT.find(keyword)
    return HttpResponse(json.dumps(items), content_type="application/json")
