from celery import task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)
import logging
logger.setLevel(logging.DEBUG)


@task
def backup():
    import os
    logger.info("Start backuping")
    os.system("python manage.py dbbackup")
    logger.info("Stop backuping")
