# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand

from xml.dom import minidom
from catalog.models import Catalog
from django.db import connection
from catalog.tasks import import_new
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Start .....")
        import_new.delay()
        logger.info("Done.....")
