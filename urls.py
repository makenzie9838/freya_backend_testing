from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/', include('freya_backend_testing.urls')),
    path('admin/', admin.site.urls),
]