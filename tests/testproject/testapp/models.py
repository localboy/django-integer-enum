from django.db import models

from django_integer_enum import fields

from .enums import JobStatus

class Job(models.Model):
    """ A test model to test Enum functionality. """
    status = fields.EnumIntegerField(enum_choices=JobStatus, default=JobStatus.DRAFT)

    def is_pending(self):
        return self.status == JobStatus.PENDING

    def activate(self):
        self.status = JobStatus.ACTIVE
        self.save()
