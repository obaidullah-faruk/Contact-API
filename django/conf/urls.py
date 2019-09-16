from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('contact/api', include('contact.urls')),
    path('admin/', admin.site.urls),
]
