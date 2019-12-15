from django.utils import timezone as tz
from django.core.mail import send_mail

import requests

from employee_management_project.celery_app import app

from .models import Employee, WorkPlace, Statistics
from .models import APPROVED


@app.task(name='management_app.tasks.register_employees')
def register_employees():
    url = 'https://jsonplaceholder.typicode.com/users'
    resp = requests.get(url)
    persons_list = resp.json()

    for person in persons_list:
        Employee.objects.create(
            name=person['name']
        )


@app.task(name='management_app.tasks.create_statistics')
def create_statistics():
    workplaces = WorkPlace.objects.filter(status=APPROVED)
    date_now = tz.localdate()

    for workplace in workplaces:
        hours_total = 0
        last_7days_worktimes = workplace.worktimes.filter(
            date__gte=date_now-tz.timedelta(7),
            date__lt=date_now,
        )

        for worktime in last_7days_worktimes:
            hours_total += worktime.hours_worked

        Statistics.objects.create(
            workplace=workplace,
            hours_total=hours_total,
        )


@app.task(name='management_app.tasks.send_mail')
def send_mail():
    print('Mail has been sent')
    return 'Mail return'
