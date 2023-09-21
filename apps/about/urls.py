from django.urls import path

from . import api_endpoints as views

app_name = 'about'

urlpatterns = [
    path('ad_banner/list/', views.AdBannerListAPIView.as_view(), name='ad_banner_list'),
    path('contact/list/', views.ContactListAPIView.as_view(), name='contact_list'),
    path('fqa/list/', views.FQAListAPIView.as_view(), name='fqa_list'),
    path('resume/create/', views.ResumeCreateAPIView.as_view(), name='resume_create'),
    path('static_text/list/', views.StaticTextListAPIView.as_view(), name='static_text_list'),
    path('vacancy/list/', views.VacancyListAPIView.as_view(), name='vacancy_list')
]
