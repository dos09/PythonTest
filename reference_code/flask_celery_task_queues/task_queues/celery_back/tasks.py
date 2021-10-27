import time

from celery import Celery

from task_queues.celery_back import celeryconfig

celery_app = Celery('tasks')
celery_app.config_from_object(celeryconfig)
# celery_app.conf.broker_transport_options = {'visibility_timeout': 5}
# TODO: remove or comment-out once done testing
# print('celery_app.conf.broker_transport_options = %s' %
#       celery_app.conf.broker_transport_options)


@celery_app.task()
def task_hello_world():
    print('Hello World (printed from tasks.py)')
    seconds = 10
    print('Will sleep for %s seconds' % seconds)
    time.sleep(seconds)
    print('Done sleeping')
    return 'Hello world (returned from tasks.py -> task_hello_world)'


@celery_app.task()
def task_fast():
    seconds = 2
    print('fast task started, will sleep for %s seconds' % seconds)
    time.sleep(seconds)
    print('fast task done sleeping')


@celery_app.task()
def task_slow():
    seconds = 20
    print('slow task started, will sleep for %s seconds' % seconds)
    time.sleep(seconds)
    print('slow task done sleeping')


@celery_app.task()
def task_banana():
    print('banana task')
