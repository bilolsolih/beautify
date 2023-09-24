from django.contrib import admin

from .models import Vacancy, StaticText, FQA, AdBanner, Resume, Contact


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location', 'vacancies', 'is_active']
    list_display_links = ['id', 'title']
    list_editable = ['vacancies', 'is_active']
    list_filter = ['is_active']


@admin.register(StaticText)
class StaticTextAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    list_display_links = ['id', 'type']
    list_filter = ['type']


@admin.register(FQA)
class FQAAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'question', 'answer']
    list_display_links = ['id']
    list_filter = ['type']
    list_editable = ['type', 'question', 'answer']


@admin.register(AdBanner)
class AdBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'link', 'is_active']
    list_display_links = ['id', 'title']
    list_filter = ['is_active']
    list_editable = ['photo', 'link', 'is_active']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'email', 'vacancy']
    list_display_links = ['id', 'full_name']
    list_filter = ['vacancy']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone_number']
    list_display_links = ['id']
    list_editable = ['full_name', 'email', 'phone_number']
# Register your models here.
