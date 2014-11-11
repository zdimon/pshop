# -*- coding: utf-8 -*-
from celery import task
from celery.utils.log import get_task_logger
import time
import hashlib
from registration.models import RegistrationProfile
logger = get_task_logger(__name__)
from config.settings import SECRET, MIRROR_ID, REGISTRATION_URL
from django.utils import simplejson

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
    logger.info('request %s' % (url,))
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    logger.info(url)
    r = requests.post(url, data=json.dumps(data), headers=headers)
    data = simplejson.loads(r.content)
    #import pdb; pdb.set_trace()
    pressa_id = data['user_id']
    pr = RegistrationProfile.objects.get(user=user)
    pr.pressa_id = data['user_id']
    pr.save()
