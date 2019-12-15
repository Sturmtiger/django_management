from django.test import TestCase
from django.urls import reverse
from django.utils import timezone as tz

from ..models import Company, Job, WorkPlace, Employee


class CompaniesListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
            weekly_hours_limit=40,
        )
        cls.companies_list_url = reverse('companies_list')

    def test_companies_list_GET(self):
        resp = self.client.get(self.companies_list_url)

        self.assertEqual(resp.status_code, 200)
        self.assertEquals(resp.context['companies'].count(), 1)


class EmployeesListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employees_list_url = reverse('employees_list')

    def test_employees_list_GET(self):
        resp = self.client.get(self.employees_list_url)

        self.assertEqual(resp.status_code, 200)


class CompanyDetailsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
            weekly_hours_limit=40,
        )
        cls.company_details_url = reverse(
            'company_details', kwargs={'pk': cls.company.id})

    def test_company_details_GET(self):
        resp = self.client.get(self.company_details_url)

        self.assertEqual(resp.status_code, 200)


class CompanyManagersListTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
            weekly_hours_limit=40,
        )
        cls.company_managers_list_url = reverse(
            'company_managers_list', kwargs={'company_id': cls.company.id})

    def test_company_managers_list_GET(self):
        resp = self.client.get(self.company_managers_list_url)

        self.assertEqual(resp.status_code, 200)


class CreateJobTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
            weekly_hours_limit=40,
        )
        cls.job_create_url = reverse(
            'job_create', kwargs={'company_id': cls.company.id})

    def test_create_job_GET(self):
        resp = self.client.get(self.job_create_url)

        self.assertEqual(resp.status_code, 200)

    def test_create_job_POST(self):
        resp = self.client.post(self.job_create_url, {
            'company': self.company.id,
            'name': 'Python Developer',
        })

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(self.company.jobs.last().name, 'Python Developer')

    def test_create_job_POST_no_data(self):
        resp = self.client.post(self.job_create_url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.company.jobs.count(), 0)


class HireEmployeeViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
            weekly_hours_limit=40,
        )
        cls.job = Job.objects.create(
            company=cls.company,
            name='Python Developer',
        )
        cls.workplace = WorkPlace.objects.create(
            job=cls.job,
        )
        cls.employee = Employee.objects.create(
            name='James Bondarchuk',
        )
        cls.workplace_hire_url = reverse(
            'workplace_hire', kwargs={'pk': cls.workplace.id})

    def test_hire_employee_GET(self):
        resp = self.client.get(self.workplace_hire_url)

        self.assertEqual(resp.status_code, 200)

    # dont work correctly
    def test_hire_employee_POST(self):
        self.assertIsNone(self.workplace.employee)
        resp = self.client.post(self.workplace_hire_url, {
            'employee': self.employee.id,
        })
        self.assertEqual(resp.status_code, 302)
        self.workplace.refresh_from_db()
        self.assertEqual(self.workplace.employee, self.employee)


class CreateWorkTimeViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
            weekly_hours_limit=40,
        )
        cls.job = Job.objects.create(
            company=cls.company,
            name='Python Developer',
        )
        cls.employee = Employee.objects.create(
            name='James Bondarchuk',
        )
        cls.workplace = WorkPlace.objects.create(
            job=cls.job,
            employee=cls.employee,
        )
        cls.worktime_create_url = reverse(
            'worktime_create', kwargs={'workplace_id': cls.workplace.id})

    def test_create_worktime_GET(self):
        resp = self.client.get(self.worktime_create_url)

        self.assertEqual(resp.status_code, 200)

    def test_date_is_less_today(self):
        resp = self.client.post(self.worktime_create_url, {
            'workplace': self.workplace.id,
            'date': tz.localdate() - tz.timedelta(2),
            'hours_worked': '12',
        })

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.workplace.worktimes.count(), 0)

    def test_create_worktime(self):
        resp = self.client.post(self.worktime_create_url, {
            'workplace': self.workplace.id,
            'date': tz.localdate(),
            'hours_worked': '12',
        })

        self.assertEqual(self.workplace.worktimes.count(), 1)
        self.assertEqual(resp.status_code, 302)
