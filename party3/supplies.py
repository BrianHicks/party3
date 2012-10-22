'party supplies!'
import imp
import os
from party3.celery import celery

@celery.task
def notify(msg):
    'notify concerned parties of a change in status'
    print msg

@celery.task
def check_service(service, path='party3/services'):
    'check a service'
    fp, pathname, description = imp.find_module(service, [path])

    try:
        imp.load_module(service, fp, pathname, description).run()
    finally:
        if fp:
            fp.close()

@celery.task
def queue_checks():
    'start checks, loading from the environment'
    try:
        services = os.environ['PARTY3_SERVICES'].split(',')
    except KeyError:
        msg = 'PARTY3_SERVICES is not set'
        notify.delay(msg)
        raise ValueError(msg)

    for service in services:
        check_service.delay(service)
