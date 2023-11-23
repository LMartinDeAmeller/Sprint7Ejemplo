from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from home.views import Home
from registration.views import loginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('clientes/', include('django.contrib.auth.urls')),
]