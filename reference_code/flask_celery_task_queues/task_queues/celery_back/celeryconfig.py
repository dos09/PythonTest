# from kombu import Queue
# broker responsible for delivering messages to celery
broker_url = 'redis://localhost:6379/0'
# if you want to read task's state, result
result_backend = 'redis://localhost:6379/0'
# enable task state reporting
task_track_started = True
# number of worker processes
worker_concurrency = 1
task_create_missing_queues = True  # true by default, but prefer to be explicit
# task_queues = ( # when this is used, the tasks go to queue "celery", the default one and are not processed
#     Queue('default_queue'),
#     Queue('slow_queue'),
# )
task_routes = {
    '*hello_world': {'queue': 'hello-q'},
    '*_slow': {'queue': 'slow-q'}
}

# TODO: comment-out when done testing
#result_backend_transport_options = {'visibility_timeout': 5}
