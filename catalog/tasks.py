# -*- coding: utf-8 -*-
from celery import task
import logging
from celery.utils.log import get_task_logger
import time
import hashlib
from registration.models import RegistrationProfile
logger = get_task_logger(__name__)
from config.settings import SECRET, MIRROR_ID, REGISTRATION_URL
from django.utils import simplejson
logger.setLevel(logging.DEBUG)
from django.core.exceptions import ObjectDoesNotExist
from config.local import  IMPORT_JOURNAL_URL
from xml.dom import minidom



@task(name='reg')
def reg(user):
    logger.info('Start registering')
    print 'Start registering'
    import requests
    import json
    url = REGISTRATION_URL
    sign = hashlib.md5(SECRET+user.username).hexdigest()
    data = {'username': user.username, 'email': user.email, 'mirror_id': MIRROR_ID, 'sign': sign}
    #import pdb; pdb.set_trace()
    print 'ssss'+url
    print 'username:%s;email:%s;mirror_id:%s;sign:%s' % (user.username, user.email, MIRROR_ID, sign)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    logger.info(url)
    r = requests.post(url, data=json.dumps(data), headers=headers)
    dt = simplejson.loads(r.content)
    #import pdb; pdb.set_trace()
    print dt
    pr = RegistrationProfile.objects.get(user=user)
    pr.pressa_id = dt['user_id']
    pr.save()
    



@task(name='import_now')
def import_now(issue_id):
    from catalog.models import ImportLog
    from catalog.models import Issue, Journal
    from config.local import IMPORT_NOW_JOURNAL_ISSUE, IMPORT_COVER_DOMAIN
    from xml.dom import minidom
    import urllib2
    import tempfile
    from django.core import files
    import requests
    import time
    
    
    #Issue.objects.all().delete()
    # http://pressa.ru/new_journal_issue
    url = IMPORT_NOW_JOURNAL_ISSUE+'/'+str(issue_id)
    logger.info('Start importing NOW from %s' % url)
    try:
        doc = urllib2.urlopen(url)
        #logger.warning('load %s' % IMPORT_NEW_JOURNAL_ISSUE)
        dom = minidom.parse(doc)
    except:
        logger.error('cant load %s' % url)
        return True
    items = dom.getElementsByTagName('issue')
    #import pdb; pdb.set_trace()
    for issue in items:
        try:
            jjj = Issue.objects.get(original_id=issue.getAttribute('id'))
            logger.info('I found issue %s!!!!!' % issue.getAttribute('id'))
        except:
            logger.info('Can not find issue %s' % issue.getAttribute('id'))
            try:
                i = Journal.objects.get(original_id=issue.getAttribute('journal_id'))
                logger.info('I found journal %s' % i.name)
            except ObjectDoesNotExist:
                logger.info('I can not find journal %s' % issue.getAttribute('journal_id'))
                i = add_new_journal(issue.getAttribute('journal_id'))         
            logger.info('Start to create issue %s' % issue.getAttribute('name'))      
            iss = Issue()
            iss.name = issue.getAttribute('name')
            iss.original_id = issue.getAttribute('id')
            iss.date = issue.getAttribute('release_date')
            iss.journal = i
            iss.is_empty = False
            iss.is_archive = False
            iss.save()
            image_url = IMPORT_COVER_DOMAIN+issue.getAttribute('cover')
            logger.info('Dowload cover from %s' % image_url) 
            try:
                request = requests.get(image_url, stream=True)
                if request.status_code != requests.codes.ok:
                    continue
            except:
                continue
            file_name = image_url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in request.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
            iss.cover.save(file_name, files.File(lf))
            i.last_issue_id = issue.getAttribute('id')
            i.cover.save(file_name, files.File(lf))
            i.save()
            i.set_archive()
            logger.info("adding...%s" % iss.name) 
            logger.info('Create record in log about issue %s' % iss.journal.name) 
            l = ImportLog()
            l.issue = iss
            l.journal = iss.journal
            l.save()
            logger.info("Finishing proccess!!") 
    logger.info("Done...")   





    
@task(name='import_new')
def import_new(date=None):
    from catalog.models import Issue, Journal
    from config.local import IMPORT_NEW_JOURNAL_ISSUE, IMPORT_COVER_DOMAIN
    from xml.dom import minidom
    import urllib2
    import tempfile
    from django.core import files
    import requests
    import time
    if not date:
        date = time.strftime("%Y-%m-%d")
    
    logger.info('Start importing from %s' % IMPORT_NEW_JOURNAL_ISSUE)
    #Issue.objects.all().delete()
    # http://pressa.ru/new_journal_issue
    try:
        doc = urllib2.urlopen(IMPORT_NEW_JOURNAL_ISSUE+'/'+date)
        #logger.warning('load %s' % IMPORT_NEW_JOURNAL_ISSUE)
        dom = minidom.parse(doc)
    except:
        logger.error('cant load %s' % IMPORT_NEW_JOURNAL_ISSUE)
        return True
    items = dom.getElementsByTagName('issue')
    #import pdb; pdb.set_trace()
    for issue in items:
        try:
            jjj = Issue.objects.filter(original_id=issue.getAttribute('id')).get()
        except:
            try:
                i = Journal.objects.filter(original_id=issue.getAttribute('journal_id')).get()
            except ObjectDoesNotExist:
                i = add_new_journal(issue.getAttribute('journal_id'))               
            iss = Issue()
            iss.name = issue.getAttribute('name')
            iss.original_id = issue.getAttribute('id')
            iss.date = issue.getAttribute('release_date')
            iss.journal = i
            iss.is_empty = False
            iss.is_archive = False
            iss.save()
            image_url = IMPORT_COVER_DOMAIN+issue.getAttribute('cover')
            try:
                request = requests.get(image_url, stream=True)
                if request.status_code != requests.codes.ok:
                    continue
            except:
                continue
            file_name = image_url.split('/')[-1]
            lf = tempfile.NamedTemporaryFile()
            for block in request.iter_content(1024 * 8):
                if not block:
                    break
                lf.write(block)
            iss.cover.save(file_name, files.File(lf))
            i.last_issue_id = issue.getAttribute('id')
            i.cover.save(file_name, files.File(lf))
            i.save()
            i.set_archive()
            logger.info("adding...%s" % iss.name) 

    logger.info("Done...")   
    
    
def add_new_journal(journal_id):    
    #import pdb; pdb.set_trace() 
    from catalog.models import Journal
    import urllib2
    doc = urllib2.urlopen(IMPORT_JOURNAL_URL+'/'+journal_id)
    dom = minidom.parse(doc)    
    items=dom.getElementsByTagName('journal')
    #import pdb; pdb.set_trace() 
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
        j.seo_title_en =  u'%s - on-line library of Armenian and foreign printed Mass Media' % (j.name_en) 
        j.seo_title_ru = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ' % (j.name_ru)
        j.seo_title_hy = u'%s - Онлайн библиотека армянских и зарубежных печатных СМИ' % (j.name_hy)
        
        j.save()
        logger.info("adding...%s" % j.name)    
        return j
        
        
    
@task(name='recount_prices')
def recount_prices(history):   
    print 'ffffff'
    from catalog.models import Journal
    print 'ddddddddddddddd-%s' % (history.pk)     
    for j in Journal.objects.filter(recount=False).order_by('-id'):
        j.price_dram = float(history.rub2dram)*float(j.price)
        j.price_usd = float(j.price_dram)/float(history.dram2usd)
        j.save()
        print str(j.id) + '...done' 
        
            
