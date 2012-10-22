from __future__ import absolute_import

from celery import Celery

celery = Celery(
    'party3.celery',
    broker='redis://',
    backend='redis://',
    include['party3.tasks']
)

celery.conf.update(
    CELERY_IGNORE_RESULTS=True
)
