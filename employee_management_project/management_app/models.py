from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('details', kwargs={'id': self.id})

    def __str__(self):
        return f'"{self.name}"(id:{self.id}) the Company'

    class Meta:
        verbose_name_plural = 'Companies'


class Manager(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}(id:{self.id}) the Manager at {self.company}'


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}(id:{self.id}) the Job at {self.company}'


class WorkPlace(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'Work place(id:{self.id}) of {self.job}'
    

class Employee(models.Model):
    work_place = models.OneToOneField(
        WorkPlace,
        on_delete=models.CASCADE, 
        )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}(id:{self.id}) the Employee of {self.work_place}'