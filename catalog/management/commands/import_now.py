# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand

from xml.dom import minidom
from catalog.models import Catalog
from django.db import connection
from catalog.tasks import import_now
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from optparse import make_option

class Command(BaseCommand):
    import time
    option_list = BaseCommand.option_list + (
        make_option("-d", "--data",
                    dest="date",
                    default = str(time.strftime("%Y-%m-%d"))),
        )
    def handle(self, *args, **options):
        logger.info("Start .....")
        date = str(options['date'])
        import_now(66123)
        #import_new(date)
        logger.info("Done.....")
