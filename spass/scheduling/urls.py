from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients_list, name='patients'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('patients/create/', views.create_patient, name='create_patient'),
    path('patients/update/<int:id>', views.update_patient, name='update_patient'),
    path('patients/delete/<int:id>', views.delete_patient, name='delete_patient'),
    path('doctors/create/', views.create_doctor, name='create_doctor'),
    path('doctors/update/<int:id>/', views.update_doctor, name='update_doctor'),
    path('doctors/delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
]