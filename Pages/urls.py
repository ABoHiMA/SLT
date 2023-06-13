from django.urls import path, include
from.import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path ('thx', views.Thx, name='thx'),
    path ('cacc', views.CAcc, name='CAcc'),
    path ('fdbk', views.Fdbk, name='Fdbk'),
    path ('', auth_views.LoginView.as_view(template_name='Pages/Lgn.html'), name='Login'),
]
