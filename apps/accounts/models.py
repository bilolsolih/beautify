from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers import UserManager
from apps.base.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    # AUTHENTICATION FIELDS #
    username = models.CharField(_('Unique name for the user'), max_length=64, unique=True)
    phone_number = models.CharField(_('Phone number'), max_length=15, unique=True)
    email = models.EmailField(_('Email'), unique=True)
    is_verified = models.BooleanField(_('Verified status'), default=False)
    is_active = models.BooleanField(_('Active status'), default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # PERSONAL INFO #
    full_name = models.CharField(_('Full name'), max_length=128)

    # DISTINCT FIELDS #
    is_staff = models.BooleanField(_('Staff status'), default=False)

    # ACTIVITIES
    reviewed_products = models.ManyToManyField('store.Product', related_name='reviewed_users', blank=True, through='store.Review', verbose_name=_('Reviewed products'))
    liked_products = models.ManyToManyField('store.Product', related_name='liked_users', blank=True, verbose_name=_('Liked products'))

    # OTHERS #
    objects = UserManager()

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['username']),
            models.Index(fields=['full_name'])
        ]

    def __str__(self):
        return self.username
