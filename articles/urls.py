from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Home', views.Home, name='Home'),
    path('Contacts', views.Contacts, name='Contacts'),
]
