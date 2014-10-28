# -*- coding: utf-8 -*-
from celery import task
from celery.utils.log import get_task_logger
import time
import hashlib
logger = get_task_logger(__name__)
from config.settings import SECRET, MIRROR_ID, REGISTRATION_URL


@task(name='reg')
def reg(user):
    logger.info('Start registering')
    print 'Start registering'
    import requests
    import json
    url = REGISTRATION_URL
    sign = hashlib.md5(SECRET+user.username).hexdigest()
    data = {'username': user.username, 'email': user.email, mirror_id: MIRROR_ID, 'sign': sign}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
