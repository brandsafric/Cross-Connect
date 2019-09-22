from django.urls import path, include
from crm import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('<int:id>', views.contact_detail, name='contact_detail'),
    path('add', views.add_contact, name='add_contact')
]
