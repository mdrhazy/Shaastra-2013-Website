from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from events.models import *
from operator import attrgetter

# Create your views here.

def events(request, event_name):
    event_name = event_name.replace("-"," ")
    event = Event.objects.get(title=event_name)
    initial = Update.objects.all()
    update = sorted(initial, key=attrgetter('id'), reverse=True)
    tab_set = event.tab_set.all()
    return render_to_response('events/events.html',locals(), context_instance= RequestContext(request))

def tabs(request, event_name, tab_name):
    event = Event.objects.get(title=event_name)
    tab_set = event.tab_set.all()
    tab = tab_set.get(title = tab_name)
    file_set = tab.tabfile_set.all()
    return render_to_response('events/tabs.html',locals(), context_instance= RequestContext(request))