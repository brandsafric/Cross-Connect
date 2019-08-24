from django.urls import path, include
from church import views

urlpatterns = [
    path('add', views.add_church, name='add_church'),
    path('services/add', views.add_service_template, name='add_service_template'),
    path('service/add', views.add_service, name='add_service'),
    path('services/<int:id>', views.service_template, name='service_template'),
    path('service/<int:id>', views.service_detail, name='service_detail')

]
