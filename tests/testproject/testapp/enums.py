from django.utils.translation import gettext as _
from django_integer_enum import enums


class JobStatus(enums.Enum):
    DRAFT = 0
    PENDING = 1
    ACTIVE = 2

    local = (
        _('Draft'),
        _('Pending'),
        _('Active')
    )
