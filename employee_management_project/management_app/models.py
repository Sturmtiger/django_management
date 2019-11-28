from django.db import models
from django.shortcuts import reverse

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

    def __str__(self):
        return f'Work place(id:{self.id}) of {self.job}'

    class Meta:
        ordering = ['-employee']
