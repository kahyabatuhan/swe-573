from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics
import json
from .twtwrapper import TWT
from profiles.records import Record

@csrf_protect
def twt_search(request):
    keyword = request.GET["q"]
    items = TWT.find(keyword)

    raw_data = serializers.serialize('python', Record.objects.filter(owner_id = request.user.id)) 
    repo = []
    for d in raw_data:
        repo.append(d['fields']['tweet'])

    refineItems = []
    for elm in items:
        if elm['name'] not in repo:
            refineItems.append(elm)
            
    return HttpResponse(json.dumps(refineItems), content_type="application/json")

@csrf_protect
def twt_save(request):
    #keyword = request.GET["q"]
    #print ('Raw Data:', request.body) 
    json_data = json.loads(request.body)
    json_data = json_data['list']
    for elm in json_data:
    	rec = Record(tweet=elm['tw'],score=elm['score'],owner=request.user)
    	rec.save()
    return HttpResponse(json.dumps("Successfuly saved"), content_type="application/json")

@csrf_protect
def twt_delete(request): 
    json_data = json.loads(request.body)
    json_data = json_data['list']
    for elm in json_data:
    	rec = Record.objects.get(tweet=elm['tw'], owner = request.user)
    	rec.delete()
    return HttpResponse(json.dumps("Successfuly deleted"), content_type="application/json")

@csrf_protect
def twt_hist(request):
	raw_data = serializers.serialize('python', Record.objects.filter(owner = request.user)) 
	#raw_data = serializers.serialize('python', Record.objects.filter(owner_id = 8)) 
	actual_data = [d['fields'] for d in raw_data]
	return HttpResponse(json.dumps(actual_data), content_type="application/json")
