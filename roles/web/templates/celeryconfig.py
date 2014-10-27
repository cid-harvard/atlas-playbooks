CELERY_IMPORTS = ('atlas.celery_tasks',)

BROKER_URL = "{{atlas_celery_broker_url}}"
CELERY_RESULT_BACKEND = "{{atlas_celery_result_backend}}"
CELERY_TASK_SERIALIZER = "msgpack"

CELERYD_CONCURRENCY = 3

from kombu import Exchange, Queue
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('prerender_queue', routing_key='prerender_route'),
)
CELERY_ROUTES = {
    'atlas.celery_tasks.prerender': {'queue': 'prerender_queue'}
}
