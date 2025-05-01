from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miApp.urls')),  # Aquí se incluyen las URLs de tu app 'miApp'
]
