from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients_list, name='patients'),
    path('doctors/', views.doctors_list, name='doctors')
]