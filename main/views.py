from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
# Create your views here.
def home(request):
    context = {}
    return render_to_response('main/home.html', context, RequestContext(request))