from django.db import models

# Create your models here.


class Company(models.Model):
    """Company model."""
    name = models.CharField(max_length=100)

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
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}(id:{self.id}) '
        'the Manager at {self.company}'


class Employee(models.Model):
    """Employee model."""
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}(id:{self.id}) the Employee'


class Job(models.Model):
    """Job model."""
    company = models.ForeignKey(
        Company,
        related_name='jobs',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}(id:{self.id}) the Job at {self.company}'


class WorkPlace(models.Model):
    """Work place model."""
    job = models.ForeignKey(
        Job,
        related_name='workplaces',
        on_delete=models.CASCADE)
    employee = models.OneToOneField(
        Employee,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        )
    
    STATUSES = [
        ('N', 'New'),
        ('A', 'Approved'),
        ('C', 'Cancelled'),
        ('F', 'Finished'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUSES,
        default='N',
        )

    def __str__(self):
        return f'Work place(id:{self.id}) of {self.job}'

    class Meta:
        ordering = ['-employee']


class WorkTime(models.Model):
    """Worktime model."""
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='worktimes',
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='worktimes',
    )
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    STATUSES = [
        ('N', 'New'),
        ('A', 'Approved'),
        ('C', 'Cancelled'),
    ]
    status = models.CharField(
        max_length=1,
        choices=STATUSES,
        default='N',
        )
