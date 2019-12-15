import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'employee_management_project.settings')

app = Celery('tasks')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
