# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.conf import settings
from django.utils.translation import check_for_language
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import translation
from page.models import Page
from registration.forms import RegistrationForm
# Create your views here.
def home(request):
    try:
        page = Page.objects.get(slug='home')
    except:
        page = None
        
    context = {'page': page, 'form': RegistrationForm()}
    return render_to_response('main/home.html', context, RequestContext(request))
    
def change_language(request):
    _next = request.REQUEST.get('next', None)
    if not _next:
        _next = request.META.get('HTTP_REFERER', None)

    if not _next:
        _next = '/'

    # если уже есть языковой префикс URL, надо убрать его
    #import pdb; pdb.set_trace()
    #settings.LANGUAGES = settings.LANGUAGES 
    for supported_language in settings.LANGUAGES:
        prefix = '/%s/' % supported_language[0]
        if _next.startswith(prefix):
            _next = _next[len(prefix):]
            break

    language = request.REQUEST.get(u'language', None)
    #if language and check_for_language(language):
    if _next == '/':
        response = HttpResponseRedirect('/')
    else:
        response = HttpResponseRedirect('/%s/%s' % (language, _next))

    if hasattr(request, 'session'):
        request.session['django_language'] = language
    else:
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)

    translation.activate(language)
    return response
    #else:
    #    return HttpResponse(status=400)
