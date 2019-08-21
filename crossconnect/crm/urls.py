from django.urls import path, include
from crm import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('add', views.add_contact, name='add_contact')
]
