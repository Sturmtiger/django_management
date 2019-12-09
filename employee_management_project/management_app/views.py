import logging

from django.shortcuts import get_object_or_404
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, FormView)
from .models import (Company, Manager,
                     Employee, Job, WorkPlace, WorkTime)
from .forms import WorkTimeForm


sentry_logger = logging.getLogger('sentry_logger')

# Create your views here.


class CompaniesListView(ListView):
    """Companies list View."""
    model = Company
    template_name = 'management_app/companies_list.html'
    context_object_name = 'companies'


class CompanyDetailsView(DetailView):
    """Companies details View."""
    model = Company
    template_name = 'management_app/company_details.html'


class CompanyManagersListView(ListView):
    """Company managers View."""
    model = Manager
    template_name = 'management_app/managers_list.html'
    context_object_name = 'managers'

    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('company_id'))
        return Manager.objects.filter(company=company)


class CreateJobView(CreateView):
    """Create job View."""
    model = Job
    fields = ['company', 'name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_initial(self):
        company = get_object_or_404(Company, id=self.kwargs.get('company_id'))
        return {'company': company}

    def get_success_url(self):
        return self.request.GET.get('next', '/')

    def form_valid(self, form):
        self.object = form.save()

        posted_data = self.request.POST
        sentry_logger.debug(
            'Job data',
            extra={
                'company_id': posted_data['company'],
                'job_name': posted_data['name']
            }
        )
        sentry_logger.info('Created Job')

        return super().form_valid(form)


class EmployeesListView(ListView):
    """Employees list View."""
    model = Employee
    template_name = 'management_app/employees_list.html'
    context_object_name = 'employees'


class EmployeeDetailsView(DetailView):
    """Employee details View."""
    model = Employee
    template_name = 'management_app/employee_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.get_object()  # employee object
        context['workplaces'] = WorkPlace.objects.filter(employee=employee)
        return context


class HireEmployeeView(UpdateView):
    """Hire employee View."""
    model = WorkPlace
    fields = ['employee']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        return self.request.GET.get('next', '/')

    def form_valid(self, form):
        self.object = form.save()

        posted_data = self.request.POST
        if posted_data['employee']:
            sentry_logger.debug(
                'Employee data',
                extra={
                    'employee_id': posted_data['employee'],
                }
            )
            sentry_logger.info('Hired employee')

        return super().form_valid(form)


class CreateWorkTimeView(FormView):
    """Create worktime View."""
    form_class = WorkTimeForm
    template_name = 'management_app/worktime_form.html'

    def get_initial(self):
        workplace = get_object_or_404(Job, id=self.kwargs.get('workplace_id'))
        return {'workplace': workplace}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        return self.request.GET.get('next', '/')

    def form_valid(self, form):
        self.object = form.save()

        posted_data = self.request.POST
        sentry_logger.debug(
            'Worktime data',
            extra={
                'workplace_id': posted_data['workplace'],
                'date_start': posted_data['date_start'],
                'date_end': posted_data['date_end'],
            }
        )
        sentry_logger.info('Hired employee')

        return super().form_valid(form)
