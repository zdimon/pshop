# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import IMPORT_CATALOG_URL
from xml.dom import minidom
from catalog.models import Catalog
from django.db import connection

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Clear catalog table.....")
        Catalog.objects.all().delete()
        logger.info("Start loading.....")
        import urllib2
        doc = urllib2.urlopen(IMPORT_CATALOG_URL)
        dom = minidom.parse(doc)
        items=dom.getElementsByTagName('genre')
        for i in items:
            c = Catalog()
            c.original_id = i.getAttribute('id')
            c.name = i.getAttribute('title_ru')
            c.lft = i.getAttribute('lft')
            c.rght = i.getAttribute('rght')
            c.tree_id = i.getAttribute('tree_id')
            c.level = i.getAttribute('level')
            c.save()
            print i.getAttribute('id')
            logger.info("adding...%s" % c.name_slug)
        logger.info("Done")
