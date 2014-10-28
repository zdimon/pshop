# -*- coding: utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from catalog.models import Journal, Catalog, Issue, Purchase
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from datetime import datetime
import urllib2
from xml.dom import minidom
import time
from config.settings import LIQPAY_PRIVATE_KEY, LIQPAY_PUBLIC_KEY, LIQPAY_RESULT_URL, LIQPAY_SERVER_URL
from liqpay.liqpay import LiqPay
from django.utils.translation import ugettext as _
# Create your views here.


class JournalListView(ListView):
    model = Journal
    template_name = 'catalog/journal_list.html'
    paginate_by = 20
    def get_queryset(self):
        qs = self.model.objects.all()
        category_slug = self.kwargs['slug']
        cat = Catalog.objects.get(name_slug=category_slug)
        qs = qs.filter(category__in=(cat.pk,))
        return qs



class JournalDetailView(DetailView):
    model = Journal
    template_name = 'catalog/journal_detail.html'
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        try:
            obj = queryset.filter(name_slug=slug).get()
        except ObjectDoesNotExist:
            raise Http404('No found matching the query')
        return obj
    def get_context_data(self, **kwargs):
        context = super(JournalDetailView, self).get_context_data(**kwargs)
        context['issues'] = self.object.issue_set.all()
        return context


@login_required
def buy(request,id):
    issue = get_object_or_404(Issue, pk=id)
    from liqpay.models import Liqpay
    l = Liqpay()
    l.issue = issue
    l.user = request.user
    l.amount = issue.journal.price
    l.save()
    liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)

    form = liqpay.cnb_form({"amount" : "3",
                            "currency" : "RUB",
                            "description" : _(u"Payment for magazine"),
                            "order_id" : l.id,
                            "result_url": LIQPAY_RESULT_URL,
                            "server_url": LIQPAY_SERVER_URL,
                            "type" : "buy",
                            "sandbox" : "1"})
    context = {"issue": issue, 'button': form}
    return render_to_response('catalog/buy.html', context, RequestContext(request))


@login_required
def payment(request,id):
    from config.settings import PURCHASE_REQUEST_URL, PARTNER_ID, PARTNER_SECRET_KEY, GET_FILE_URL, PARTNER_NAME
    issue = get_object_or_404(Issue, pk=id)
    md5 = make_md5(str(request.user.pk),str(issue.original_id),PARTNER_SECRET_KEY)
    url = PURCHASE_REQUEST_URL+'?user=%s&price=%s&art=%s&md5=%s&mail=%s&place=%s' % (request.user.pk,issue.journal.price,issue.original_id,md5,request.user.email,PARTNER_ID)
    #import pdb; pdb.set_trace()
    out = urllib2.urlopen(url)
    dom = minidom.parse(out)
    item = list(dom.getElementsByTagName('response'))
    status = item[0].getAttribute('status')
    message = item[0].getAttribute('message')
    if status=='0':
        tm = int(time.time())
        ln =  '/'.join((GET_FILE_URL,str(tm),str(request.user.id),str(issue.original_id),str(PARTNER_NAME)))
        link = '<a href="%s" target=_blank>' % (ln,) +_(u'Link to download')+'</a>'
    else:
        link = ''
    #import pdb; pdb.set_trace()
    p = Purchase()
    p.issue = issue
    p.user = request.user
    p.price = issue.journal.price
    p.save()
    context = {"issue": issue, "message": message , "link": link}
    return render_to_response('catalog/payment_done.html', context, RequestContext(request))


def make_md5(user, art, key):
    import hashlib
    s = ":".join((user, art, key))
    print s
    #import pdb; pdb.set_trace()
    digest = hashlib.md5(s).hexdigest()
    return digest


def report(request,time,sign):
    from lxml import etree
    from config.settings import PARTNER_NAME
    response = etree.Element("partner-sales")
    response.set("checkpoint", str(time))
    response.set("timestamp", str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    response.set("partnemr", str(PARTNER_NAME))
    items = Purchase.objects.all()
    for i in items:
        subelement = etree.SubElement(response, "sale")
        subelement.set("item-id", str(i.issue.id))
        subelement.set("pay-id", str(i.id))
        subelement.set("price", str(i.price))
        subelement.set("time", str(i.created.strftime("%Y-%m-%d %H:%M:%S")))
    text = etree.tostring(response, encoding="utf-8")
    http_response = HttpResponse(text, content_type="application/xml")
    http_response['Content-Length'] = len(text)
    http_response['Content-Encoding'] = "utf-8"
    return http_response
    
    
    
def reg(request):
    from django.utils import simplejson
    from django.http import HttpResponse
    import requests
    import jsons
    url = "http://localhost:8002/mirror/registration/"
    data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    some_data_to_dump = {
        'status': 0,
        'message': 'ok',
    }
    data = simplejson.dumps(some_data_to_dump)
    
    #req = urllib2.Request('http://localhost:8002/mirror/registration/')
    #req.add_header('Content-Type', 'application/json')
    #response = urllib2.urlopen(req, data)
    return HttpResponse(data, mimetype='application/json')





    
    
