# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import  IMPORT_JOURNAL_CATALOG_URL
from xml.dom import minidom
from catalog.models import Journal, Catalog
from django.db import connection

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Clear m2m table.....")
        Journal.category.through.objects.all().delete()
        logger.info("Start loading.....")
        cat = Catalog.objects.all()
        for c in cat:
            logger.info("category %s" % c.pk)
            import urllib2
            url = IMPORT_JOURNAL_CATALOG_URL+'/'+str(c.original_id)
            try:
                doc = urllib2.urlopen(url)
            except:
                import pdb; pdb.set_trace()
            dom = minidom.parse(doc)
            items=dom.getElementsByTagName('journal')
            for i in items:
                id = i.getAttribute('id')
                #import pdb; pdb.set_trace()
                j = Journal.objects.get(original_id=id)
                j.category.add(c)
                logger.info("adding...%s" % j.name)
        logger.info("Done")
