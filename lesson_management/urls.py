from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('core.urls')),
    path('api/v1/students/', include('student.urls')),
    path('api/v1/teachers/', include('teacher.urls')),
]
