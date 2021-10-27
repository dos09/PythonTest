from datetime import datetime

from flask import Flask

from task_queues.celery_back import tasks

app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    tasks.task_hello_world.apply_async(
        task_id='hello'
    )
    return 'hello (returned from vanguard.py -> hello)'


@app.route('/fast', methods=['GET', 'POST'])
def fast():
    tasks.task_fast.apply_async(
        task_id='fast'
    )
    return 'fast ok'


@app.route('/slow', methods=['GET', 'POST'])
def slow():
    tasks.task_slow.apply_async(
        task_id='slow (%s)' % datetime.utcnow() # TODO: leave only "slow" when done testing
    )
    return 'slow ok'


@app.route('/banana', methods=['GET', 'POST'])
def banana():
    tasks.task_banana.apply_async(
        task_id='banana'
    )
    return 'banana ok'
