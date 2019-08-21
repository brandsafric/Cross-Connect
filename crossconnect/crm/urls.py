from django.urls import path, include
from crm import views

urlpatterns = [
    path('add', views.add_contact, name='add_contact')
]
