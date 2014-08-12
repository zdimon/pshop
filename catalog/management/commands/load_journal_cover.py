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
        import urllib2
        import tempfile
        import requests
        from django.core import files
        for j in Journal.objects.all():
            url = IMPORT_COVER_JOURNAL_URL+'/'+str(j.original_id)
            logger.info("loading xml from ...%s" % url)
            doc = urllib2.urlopen(url)
            dom = minidom.parse(doc)

            items=dom.getElementsByTagName('cover')
            for i in items:
                image_url = IMPORT_COVER_DOMAIN+i.getAttribute('url')
                logger.info("loading cover from ...%s" % image_url)
                #import pdb; pdb.set_trace()
                request = requests.get(image_url, stream=True)
                if request.status_code != requests.codes.ok:
                    continue
                file_name = image_url.split('/')[-1]
                lf = tempfile.NamedTemporaryFile()
                for block in request.iter_content(1024 * 8):
                    if not block:
                        break
                    lf.write(block)
                j.cover.save(file_name, files.File(lf))
        logger.info("Done")
