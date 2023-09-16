from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('Created date'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated date'), auto_now=True)

    class Meta:
        abstract = True
