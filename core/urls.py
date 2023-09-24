from django.contrib import admin
from django.urls import path, include

from .drf_schemas import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('api/v1/about/', include('apps.about.urls', namespace='about')),
    path('api/v1/store/', include('apps.store.urls', namespace='store')),
]

urlpatterns += swagger_patterns
