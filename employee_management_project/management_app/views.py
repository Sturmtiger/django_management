from django.shortcuts import get_object_or_404
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView)
from .models import (Company, Manager,
                     Employee, Job, WorkPlace, WorkTime)


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


class CreateWorkTimeView(CreateView):
    """Create worktime View."""
    model = WorkTime
    fields = [
        'workplace',
        'date_start',
        'date_end',
    ]

    def get_initial(self):
        workplace = get_object_or_404(Job, id=self.kwargs.get('workplace_id'))
        return {'workplace': workplace}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        return self.request.GET.get('next', '/')
