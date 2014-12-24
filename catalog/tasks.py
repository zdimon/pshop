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
    
    
@task(name='import_new')
def import_new():
    from catalog.models import Issue, Journal
    from config.local import IMPORT_NEW_JOURNAL_ISSUE, IMPORT_COVER_DOMAIN
    from xml.dom import minidom
    import urllib2
    import tempfile
    from django.core import files
    import requests
    logger.info('Start importing from %s' % IMPORT_NEW_JOURNAL_ISSUE)
    #Issue.objects.all().delete()
    try:
        doc = urllib2.urlopen(IMPORT_NEW_JOURNAL_ISSUE)
        #logger.warning('load %s' % IMPORT_NEW_JOURNAL_ISSUE)
        dom = minidom.parse(doc)
    except:
        logger.error('cant load %s' % IMPORT_NEW_JOURNAL_ISSUE)
        return True
    items = dom.getElementsByTagName('issue')
    for issue in items:
        try:
            jjj = Issue.objects.filter(original_id=issue.getAttribute('id')).get()
        except:
            i = Journal.objects.filter(original_id=issue.getAttribute('journal_id')).get()
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
            logger.info("adding...%s" % iss.name) 
    logger.info("Done...")           
