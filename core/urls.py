from django.contrib import admin
from django.urls import path

from .drf_schemas import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += swagger_patterns
