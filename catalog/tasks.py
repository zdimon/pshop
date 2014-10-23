# -*- coding: utf-8 -*-
from celery import task
from celery.utils.log import get_task_logger
import time

logger = get_task_logger(__name__)

@task(name='registration')
def reg(user):
    logger.info('Start registering')
    import requests
    import json
    url = "http://localhost:8002/mirror/registration/"
    data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
