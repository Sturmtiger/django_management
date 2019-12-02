from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView)
from .models import (Company, Manager,
                     Employee, Job, WorkPlace, WorkTime)
# from .forms import *

# Create your views here.


class CompaniesListView(ListView):
    model = Company
    template_name = 'management_app/companies_list.html'
    context_object_name = 'companies'


class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'management_app/company_details.html'


class CompanyManagersListView(ListView):
    model = Manager
    template_name = 'management_app/managers_list.html'
    context_object_name = 'managers'

    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('company_id'))
        return Manager.objects.filter(company=company)


class CreateJobView(CreateView):
    model = Job
    fields = ['company', 'name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_id'] = self.kwargs.get('company_id')
        return context

    def get_initial(self):
        company = get_object_or_404(Company, id=self.kwargs.get('company_id'))
        return {'company': company}

    def get_success_url(self):
        company_id = self.kwargs.get('company_id')
        return reverse_lazy('company_details', kwargs={'pk': company_id})


class EmployeesListView(ListView):
    model = Employee
    template_name = 'management_app/employees_list.html'
    context_object_name = 'employees'


class EmployeeDetailsView(DetailView):
    model = Employee
    template_name = 'management_app/employee_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = get_object_or_404(Employee, pk=self.kwargs.get('pk'))
        context['worktimes'] = WorkTime.objects.filter(employee=employee)
        # Jobs without Worktimes!
        context['jobs'] = Job.objects.filter(
            ~Q(worktimes__employee=employee)
        )
        return context


class HireEmployeeView(UpdateView):
    model = WorkPlace
    fields = ['employee']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_pk'] = get_object_or_404(
            WorkPlace, pk=self.kwargs.get('pk')
        ).job.company.pk
        return context

    def get_success_url(self):
        company_pk = get_object_or_404(
            WorkPlace, pk=self.kwargs.get('pk')
        ).job.company.pk
        return reverse_lazy('company_details', kwargs={'pk': company_pk})


class CreateWorkTimeView(CreateView):
    model = WorkTime
    fields = [
        'employee',
        'job',
        'date_start',
        'date_end',
    ]

    def get_initial(self):
        employee = get_object_or_404(
            Employee, id=self.kwargs.get('employee_id'))
        job = get_object_or_404(Job, id=self.kwargs.get('job_id'))
        return {'employee': employee, 'job': job}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee_id'] = self.kwargs.get('employee_id')
        return context

    def get_success_url(self):
        employee_id = self.kwargs.get('employee_id')
        return reverse_lazy('employee_details', kwargs={'pk': employee_id})