from django.urls import path, include

from users import views

urlpatterns = [
    path('register', views.add_user, name='add_user')
]
