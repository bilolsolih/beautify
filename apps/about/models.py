from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.base.models import TimeStampedModel
from . import choices


class AdBanner(models.Model):
    title = models.CharField(_('Title'), max_length=128, blank=True, null=True)
    photo = models.ImageField(_('Photo'), upload_to='images/banners/')
    link = models.URLField(_('Link'), blank=True, null=True)
    is_active = models.BooleanField(_('Active status'), default=True)

    class Meta:
        verbose_name = _('AdBanner')
        verbose_name_plural = _('AdBanners')

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.pk


class Vacancy(TimeStampedModel):
    title = models.CharField(_('Job title'), max_length=256)
    location = models.CharField(_('Location'), max_length=256)
    vacancies = models.PositiveIntegerField(_('Number of vacant positions'), blank=True, null=True)
    is_active = models.BooleanField(_('Active status'), default=True)

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')

    def __str__(self):
        return self.title


class Resume(TimeStampedModel):
    full_name = models.CharField(_('Full name'), max_length=128)
    phone_number = PhoneNumberField(_('Phone number'))
    email = models.EmailField(_('Email'), blank=True, null=True)
    vacancy = models.ForeignKey('about.Vacancy', related_name='resumes', on_delete=models.CASCADE, verbose_name=_('Vacancy'))
    resume = models.FileField(_('Resume file'), upload_to='files/resumes/%Y/%m/')
    text_resume = models.TextField(_('Text resume'))

    class Meta:
        verbose_name = _('Resume')
        verbose_name_plural = _('Resumes')

    def __str__(self):
        return f'{self.vacancy.title} - {self.full_name}'


class Contact(models.Model):
    full_name = models.CharField(_('Full name'), max_length=128)
    email = models.EmailField(_('Email'))
    phone_number = PhoneNumberField(_('Phone number'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        unique_together = ['email', 'phone_number']

    def __str__(self):
        return self.full_name


class StaticText(models.Model):
    type = models.CharField(_('Text type'), choices=choices.STATIC_TEXT, max_length=1, unique=True)
    content = RichTextField(_('Content'))

    class Meta:
        verbose_name = _('Static text')
        verbose_name_plural = _('Static texts')

    def __str__(self):
        return f'Static text - {self.type}'


class FQA(models.Model):
    class QuestionType(models.TextChoices):
        DELIVERY = ('Delivery', _('Delivery'))
        GENERAL = ('General', _('General'))

    question = models.CharField(_('Question'), max_length=512)
    answer = models.TextField(_('Answer'))
    type = models.CharField(_('Question type'), choices=QuestionType.choices, max_length=8)

    class Meta:
        verbose_name = _('FQA')
        verbose_name_plural = _('FQAs')

    def __str__(self):
        return self.question
