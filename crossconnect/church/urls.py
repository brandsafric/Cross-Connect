from django.urls import path, include
from church import views

urlpatterns = [
    path('add', views.add_church, name='add_church')
]
