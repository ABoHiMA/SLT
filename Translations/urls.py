from django.urls import path
from.import views

urlpatterns = [
    path ('trans', views.translate, name='trans'),
]
