# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import  IMPORT_JOURNAL_ISSUE, IMPORT_COVER_DOMAIN
from xml.dom import minidom
from catalog.models import Issue, Journal
from django.db import connection
import requests
import tempfile
from django.core import files
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Started.....")
        for j in Journal.objects.all():
            j.update_in_category()
            logger.info("Process %s" % j.id)
        logger.info("Stoped")
