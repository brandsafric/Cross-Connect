from django.urls import path, include

from base import views

urlpatterns = [
    path('', views.homepage, name='homepage')
]
