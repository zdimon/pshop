# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import  IMPORT_COVER_JOURNAL_URL, IMPORT_COVER_DOMAIN
from xml.dom import minidom
from catalog.models import Journal
from django.db import connection
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Start loading.....")
        for j in Journal.objects.all():
            j.set_archive()
            logger.info("making....%s" % j.name)
        logger.info("Done")
