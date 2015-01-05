# -*- coding: utf-8 -*-
import logging
logging.basicConfig()
from optparse import make_option
from django.core.management.base import BaseCommand
from config.local import  IMPORT_JOURNAL_URL, IMPORT_COVER_DOMAIN, IMPORT_COVER_JOURNAL_URL
from xml.dom import minidom
from catalog.models import Journal, Issue
from django.db import connection
import urllib2
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
import os.path
import requests
import tempfile
from django.core import files

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Start")
       
        doc = urllib2.urlopen(IMPORT_JOURNAL_URL)
        dom = minidom.parse(doc)

        items=dom.getElementsByTagName('journal')
        for i in items:
            #import pdb; pdb.set_trace() 
            try:
                j = Journal.objects.get(original_id=i.getAttribute('id'))
                j.count_for_pay = i.getAttribute('free_delta')
                #if not j.description_hy:
                j.description_hy = j.description_ru
                #if not j.description_en:
                j.description_en = j.description_ru
                if not j.seo_title_ru:
                    j.seo_title_ru = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ' % (j.name_ru)
                if not j.seo_title_en:
                    if j.name_en:
                        j.seo_title_en = u'%s - on-line library of Armenian and foreign printed Mass Media' % (j.name_en)
                    else:
                        j.seo_title_en = u'%s - on-line library of Armenian and foreign printed Mass Media' % (j.name_ru)
                if not j.seo_title_hy:
                    if j.name_hy:
                        j.seo_title_hy = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ' % (j.name_hy)
                    else:
                        j.seo_title_hy = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ' % (j.name_ru)                                     
                    
                    
                    
                    
                    
                    
                j.save()
                '''            if not os.path.isfile(j.cover.path):
                url = IMPORT_COVER_JOURNAL_URL+'/'+str(j.original_id)
                import pdb; pdb.set_trace() 
                doc = urllib2.urlopen(url)
                dom = minidom.parse(doc)                
                image_url = IMPORT_COVER_DOMAIN+i.getAttribute('url')
                import pdb; pdb.set_trace() 
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
            
            
                ''' 
                logger.info("updating...%s" % j.name)
            except:
                pass
            
           
            
        logger.info("Done")
