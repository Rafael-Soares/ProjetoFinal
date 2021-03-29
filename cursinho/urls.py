from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app1.urls')),
    path('admin/', admin.site.urls),
]
