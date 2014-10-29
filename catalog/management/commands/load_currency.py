# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import IMPORT_CATALOG_URL
from xml.dom import minidom
from catalog.models import CurrencyHistory, Journal
from django.db import connection

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):

    def handle(self, *args, **options):
        from datetime import datetime
        logger.info("Start loading.....")
        import urllib2
        doc = urllib2.urlopen('https://www.cba.am/_layouts/rssreader.aspx?rss=280F57B8-763C-4EE4-90E0-8136C13E47DA')
        dom = minidom.parse(doc)
        items=dom.getElementsByTagName('title')
        c = CurrencyHistory()
        c.date = datetime.now()
        for i in items:
            #e = i.getElementByTagName('title')
            #import pdb; pdb.set_trace()
            
            v =   i.firstChild.nodeValue
            ar = v.split('-')
            if ar[0].strip() == 'RUB':
                print ar[0]+'---'+ar[2]
                c.rub2dram = ar[2]
            if ar[0].strip() == 'USD':
                print ar[0]+'---'+ar[2]
                c.dram2usd = ar[2]
            #try:
        c.save()    
        for j in Journal.objects.all().order_by('-id'):
            j.price_dram = float(c.rub2dram)*float(j.price)
            j.price_usd = float(j.price_dram)/float(c.dram2usd)
            j.save()
            print str(j.id) + '...done'      
            #except:
            #    pass
                #import pdb; pdb.set_trace()

        logger.info("Done")
