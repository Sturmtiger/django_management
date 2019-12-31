from django.urls import path
from . import views


app_name = 'management'

urlpatterns = [
    path('',
         views.CompaniesListView.as_view(),
         name='companies_list'),
    path('company/<int:pk>/details/',
         views.CompanyDetailsView.as_view(),
         name='company_details'),
    path('company/<int:company_id>/managers/',
         views.CompanyManagersListView.as_view(),
         name='company_managers_list'),
    path('company/<int:company_id>/job-create/',
         views.CreateJobView.as_view(),
         name='job_create'),
    path('employees-list/',
         views.EmployeesListView.as_view(),
         name='employees_list'),
    path('employee/<int:pk>/details/',
         views.EmployeeDetailsView.as_view(),
         name='employee_details'),
    path('workplace/<int:pk>/hire/',
         views.HireEmployeeView.as_view(),
         name='workplace_hire'),
    path('workplace/<int:workplace_id>/worktime-create/',
         views.CreateWorkTimeView.as_view(),
         name='worktime_create'),
]
