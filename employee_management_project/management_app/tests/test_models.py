from django.test import TestCase
from django.db import IntegrityError

from ..models import Company, Job, WorkPlace, Employee, Manager


class CompanyTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
        )

    def test_unique_company_name(self):
        with self.assertRaises(IntegrityError):
            Company.objects.create(
                name='Boston Dynamics',
            )


class ManagerTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
        )
        cls.manager = Manager.objects.create(
            company=cls.company,
            name='James',
            surname='Bondov',
        )

    def test_manager(self):
        # manager belongs to the company
        self.assertEqual(self.manager.company, self.company)


class JobTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company1 = Company.objects.create(
            name='Boston Dynamics',
        )
        cls.company2 = Company.objects.create(
            name='Rudy Corporation',
        )
        cls.job = Job.objects.create(
            company=cls.company1,
            name='Engineer',
        )

    def test_unique_job_name_for_one_company(self):
        Job.objects.create(
            company=self.company2,
            name='Engineer',
        )
        with self.assertRaises(IntegrityError):
            Job.objects.create(
                company=self.company1,
                name='Engineer',
            )


class WorkPlaceTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = Company.objects.create(
            name='Boston Dynamics',
        )
        cls.job = Job.objects.create(
            company=cls.company,
            name='Engineer',
        )
        cls.employee = Employee.objects.create(
            name='John',
            surname='Smith',
        )
        cls.workplace = WorkPlace.objects.create(
            job=cls.job,
            employee=cls.employee,
        )

    def test_unique_employee_and_job(self):
        with self.assertRaises(IntegrityError):
            WorkPlace.objects.create(
                job=self.job,
                employee=self.employee
            )