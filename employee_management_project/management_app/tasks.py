from django.utils import timezone as tz
from django.core.mail import send_mail

import requests

from employee_management_project.celery_app import app

from .models import Employee, WorkPlace, Statistics
from .models import APPROVED


@app.task(name='management_app.tasks.register_employees')
def register_employees():
    """Registers employees from JSON API."""
    url = 'https://jsonplaceholder.typicode.com/users'
    resp = requests.get(url)
    persons_list = resp.json()

    for person in persons_list:
        Employee.objects.create(
            name=person['name']
        )


@app.task(name='management_app.tasks.create_statistics')
def create_statistics():
    """Creates statistics of hours
    worked per week of employees.
    Employee's workplace must have Approved
    status.
    """
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

        company = workplace.job.company
        employee_name = workplace.employee.name
        managers_emails = list(
            company.managers.values_list('email', flat=True))
        overtime_hours = hours_total - company.weekly_hours_limit
        if overtime_hours > 0:
            send_mail_if_overtime.delay(
                employee_name=employee_name,
                overtime_hours=overtime_hours,
                recipient_list=managers_emails,
            )


@app.task(name='management_app.tasks.send_mail_if_overtime')
def send_mail_if_overtime(employee_name, overtime_hours, recipient_list):
    """Sends mail to the company managers
    where the employee has overtimed
    weekly hours limit in the company.
    """
    send_mail(
        subject='Employee %s. Overtime!' % employee_name,
        message='Employee %s has overtimed the established weekly hours limit for %d.' % (
            employee_name, overtime_hours),
        from_email='dummy@gmail.com',
        recipient_list=recipient_list,
    )
