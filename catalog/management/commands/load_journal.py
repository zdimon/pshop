# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import  IMPORT_JOURNAL_URL
from xml.dom import minidom
from catalog.models import Journal, Issue
from django.db import connection

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# http://pressa.ru/journals_list

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Clear issue table.....")
        Issue.objects.all().delete()
        logger.info("Clear m2m table.....")
        Journal.category.through.objects.all().delete()
        logger.info("Clear journal table.....")
        Journal.objects.all().delete()
        logger.info("Start loading.....")
        import urllib2
        doc = urllib2.urlopen(IMPORT_JOURNAL_URL)
        dom = minidom.parse(doc)

        items=dom.getElementsByTagName('journal')
        for i in items:
            j = Journal()
            j.original_id = i.getAttribute('id')
            j.name = i.getAttribute('name')
            j.description = i.getAttribute('description')
            j.price = i.getAttribute('price')
            j.journal_type = i.getAttribute('journal_type')
            j.price_dram = 0
            j.price_usd = 0
            j.save()
            logger.info("adding...%s" % j.name)
        logger.info("Done")
