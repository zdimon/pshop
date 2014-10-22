# Create your views here.
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from page.models import Page
from datetime import date, datetime, timedelta

def home(request):
    context = {}
    try:
        page = Page.objects.get(slug='home')
        context = {"page":page}
    except:
        pass
    ycur = date.today().year
    mcur = date.today().month
    context['ycur'] = ycur
    context['mcur'] = mcur
    return render_to_response('home.html', context, RequestContext(request))


def show(request,slug):
    context = {}
    try:
        page = Page.objects.get(slug=slug)
        context = {"page":page}
    except:
        pass
    return render_to_response('show.html', context, RequestContext(request))



