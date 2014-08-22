# -*- coding: utf8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from catalog.models import Journal, Catalog, Issue, Purchase
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from config.settings import LIQPAY_PRIVATE_KEY, LIQPAY_PUBLIC_KEY, LIQPAY_RESULT_URL, LIQPAY_SERVER_URL
from liqpay import LiqPay
# Create your views here.


def result(request):
    context = {}
    return render_to_response('liqpay/result.html', context, RequestContext(request))


def server(request):
    from models import Liqpay
    import pdb; pdb.set_trace()
    l = Liqpay.objects.get(id=request.POST['order_id'])
    l.is_success = True
    l.save()
    #l = Liqpay()
    #l.save()
    context = {}
    return render_to_response('liqpay/server.html', context, RequestContext(request))
