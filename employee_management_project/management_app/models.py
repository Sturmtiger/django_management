from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Constants for status field
NEW = 'N'
APPROVED = 'A'
CANCELLED = 'C'
FINISHED = 'F'

# Create your models here.


class Company(models.Model):
    """Company model."""
    name = models.CharField(max_length=100, unique=True)
    weekly_hours_limit = models.IntegerField()

    def __str__(self):
        return f'"{self.name}"(id:{self.id}) the Company'

    class Meta:
        verbose_name_plural = 'Companies'


class Manager(models.Model):
    """Manager model."""
    company = models.ForeignKey(
        Company,
        related_name='managers',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return (f'{self.name}(id:{self.id}) '
                f'the Manager at {self.company}')


class Employee(models.Model):
    """Employee model."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}(id:{self.id}) the Employee'


class Job(models.Model):
    """Job model."""
    company = models.ForeignKey(
        Company,
        related_name='jobs',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}(id:{self.id}) the Job at {self.company}'

    class Meta:
        unique_together = ['company', 'name']


class WorkPlace(models.Model):
    """Work place model."""
    STATUS = [
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELLED, 'Cancelled'),
        (FINISHED, 'Finished'),
    ]

    job = models.ForeignKey(
        Job,
        related_name='workplaces',
        on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee,
        related_name='workplaces',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=NEW,
    )

    def __str__(self):
        return f'Work place(id:{self.id}) of {self.job}'

    class Meta:
        unique_together = ['job', 'employee']
        ordering = ['-employee']


class WorkTime(models.Model):
    """Worktime model."""
    workplace = models.ForeignKey(
        WorkPlace,
        on_delete=models.CASCADE,
        related_name='worktimes',
    )
    date = models.DateField()
    hours_worked = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(12),
        ]
    )

    def __str__(self):
        return f'WorkTime({self.id}) of {self.workplace}({self.workplace.id})'

    class Meta:
        unique_together = ['workplace', 'date']
        ordering = ['-date']


class Statistics(models.Model):
    """Statistics model.
    Object: the sum of the working hours 
    of individual employees at 7-day intervals
    and timestamp.
    """
    workplace = models.ForeignKey(
        WorkPlace,
        on_delete=models.CASCADE,
    )
    hours_total = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
