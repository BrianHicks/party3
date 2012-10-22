from __future__ import absolute_import
import os

from celery import Celery

celery = Celery(
    'party3.celery',
    broker=os.environ.get('REDISTOGO_URL', 'redis://'),
    backend=os.environ.get('REDISTOGO_URL', 'redis://'),
    include=['party3.supplies']
)

celery.conf.update(
    CELERY_IGNORE_RESULTS=True
)
