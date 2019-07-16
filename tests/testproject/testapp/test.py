from django.test import TestCase

from .enums import JobStatus
from .models import Job


class JobTestCase(TestCase):
    def setUp(self):
        self.job = Job.objects.create()

    def test_job_default(self):
        self.assertEqual(self.job.status, JobStatus.DEFAULT)

    def test_job_draft(self):
        self.assertEqual(self.job.status, JobStatus.DRAFT)

    def test_job_is_pending(self):
        self.assertFalse(self.job.status, JobStatus.PENDING)

    def test_job_is_active(self):
        self.job.activate()
        self.assertEqual(self.job.status, JobStatus.ACTIVE)


class EnumTestCase(TestCase):
    def setUp(self):
        self.enum = JobStatus()

    def test_length(self):
        self.assertEqual(len(self.enum.choices()), 3)

    def test_choices(self):
        self.assertEqual(
            self.enum.choices(), [(0, 'Draft'), (1, 'Pending'), (2, 'Active')])

    def test_default_in_key(self):
        self.assertFalse(self.enum.is_in_keys('DEFAULT'))
