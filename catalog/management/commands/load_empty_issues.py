# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import  IMPORT_JOURNAL_ISSUE, IMPORT_COVER_DOMAIN
from config.settings import BASE_DIR
from xml.dom import minidom
from catalog.models import Issue, Journal
from django.db import connection
import requests
import tempfile
from django.core import files
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import os.path

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Clear issue table.....")
        Issue.objects.all().delete()
        logger.info("iStart loading.....")
        import urllib2
        for i in Journal.objects.all():
            url = IMPORT_JOURNAL_ISSUE+'/'+str(i.original_id)+'/0'
            #import pdb; pdb.set_trace()
            try:
                doc = urllib2.urlopen(url)
            except:
                continue
            dom = minidom.parse(doc)
            items = dom.getElementsByTagName('issue')
            for issue in items:
                #import pdb; pdb.set_trace()
                iss = Issue()
                iss.name = issue.getAttribute('name')
                iss.original_id = issue.getAttribute('id')
                iss.date = issue.getAttribute('release_date')
                iss.journal = i
                
                image_url = IMPORT_COVER_DOMAIN+issue.getAttribute('cover')
                file_name = image_url.split('/')[-1]
                fpath = BASE_DIR+'/media/issue_cover/'+file_name
                if os.path.isfile(fpath):
                    print 'cover exists %s' % (fpath,)
                    iss.cover = 'issue_cover/%s' % (file_name,)
                else: 
                    try:
                        request = requests.get(image_url, stream=True)
                        if request.status_code != requests.codes.ok:
                            continue
                    except:
                        continue                
                    lf = tempfile.NamedTemporaryFile()
                    for block in request.iter_content(1024 * 8):
                        if not block:
                            break
                        lf.write(block)
                    iss.cover.save(file_name, files.File(lf))
                    print 'loading cover from %s' % (image_url,)
                iss.save()
                logger.info("adding...%s" % iss.name)
        logger.info("Done")
