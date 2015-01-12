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
# http://pressa.ru/journals_list
class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Start")
       
        doc = urllib2.urlopen(IMPORT_JOURNAL_URL+'/0')
        dom = minidom.parse(doc)

        items=dom.getElementsByTagName('journal')
        for i in items:
            #import pdb; pdb.set_trace() 
            try:
                j = Journal.objects.get(original_id=i.getAttribute('id'))
                j.count_for_pay = i.getAttribute('free_delta')
                if not j.description_hy:
                    j.description_hy = i.getAttribute('description')
                if not j.description_ru:
                    j.description_ru = i.getAttribute('description')
                if not j.description_en:
                    j.description_en = i.getAttribute('description')
                if not j.seo_title_ru:
                    j.seo_title_ru = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ' % (j.name_ru)
                if not j.seo_title_en:
                    if j.name_en:
                        j.seo_title_en = u'%s - on-line library of Armenian and foreign printed Mass Media' % (j.name_en)
                    else:
                        j.seo_title_en = u'%s - on-line library of Armenian and foreign printed Mass Media' % (j.name_ru)
                if not j.seo_title_hy:
                    if j.name_hy:
                        j.seo_title_hy = u'%s - Հայկական և արտասահմանյան տպագիր ԶԼՄ-ների առցանց գրադարան)' % (j.name_hy)
                    else:
                        j.seo_title_hy = u'%s - Հայկական և արտասահմանյան տպագիր ԶԼՄ-ների առցանց գրադարան)' % (j.name_ru)                                     
                    
                
                j.seo_title_hy = u'%s - Հայկական և արտասահմանյան տպագիր ԶԼՄ-ների առցանց գրադարան | Pressinfo.am' % (j.name_hy)
                #j.seo_title_hy = u'%s - Հայկական և արտասահմանյան տպագիր ԶԼՄ-ների առցանց գրադարան | Pressinfo.am' % (j.name_hy)                     
                    
                    
                    
                    
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
            except Exception as e:
                print e
                print 'id === %s' % (str(i.getAttribute('id')),)
                doc = urllib2.urlopen(IMPORT_JOURNAL_URL+'/'+i.getAttribute('id'))
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
                    j.last_issue_id = 0
                    j.count_for_pay = i.getAttribute('free_delta')
                    j.name_ru = i.getAttribute('name')
                    j.name_en = i.getAttribute('name')
                    j.name_hy = i.getAttribute('name')
                    j.description_hy = i.getAttribute('description')
                    j.description_ru = i.getAttribute('description')
                    j.description_en = i.getAttribute('description')
                    j.seo_title_en =  u'%s - on-line library of Armenian and foreign printed Mass Media | pressinfo.am' % (j.name_en) 
                    j.seo_title_ru = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ | pressinfo.am' % (j.name_ru)
                    j.seo_title_hy = u'%s - Հայկական և արտասահմանյան տպագիր ԶԼՄ-ների առցանց գրադարան | pressinfo.am' % (j.name_hy)
                    logger.info("adding...%s" % j.name)                
                
                
                
                #raise
            
           
            
        logger.info("Done")
