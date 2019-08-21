from django.urls import path, include
from church import views

urlpatterns = [
    path('add', views.add_church, name='add_church'),
    path('services/template', views.add_service_template, name='add_service_template'),
    path('services/add', views.add_service, name='add_service')
]
