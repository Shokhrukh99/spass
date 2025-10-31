from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patients_list, name='patients'),
    path('doctors/', views.doctors_list, name='doctors'),
    path('services/', views.services_list, name='services'),
    # --- PATIENTS ---
    path('patients/create/', views.create_patient, name='create_patient'),
    path('patients/update/<int:id>', views.update_patient, name='update_patient'),
    path('patients/delete/<int:id>', views.delete_patient, name='delete_patient'),
    # --- DOCTORS ---
    path('doctors/create/', views.create_doctor, name='create_doctor'),
    path('doctors/update/<int:id>/', views.update_doctor, name='update_doctor'),
    path('doctors/delete/<int:id>/', views.delete_doctor, name='delete_doctor'),
    # ---SERVICES ---
    path('services/create/', views.create_service, name='create_service'),
    path('services/update/<int:id>/', views.update_service, name='update_service'),
    path('services/delete/<int:id>/', views.delete_service, name='delete_service'),
    # --- APPOINTMENTS ---
    path('appointments/', views.AppointmentListView.as_view(), name='appointments'),
    path('appointments/create/', views.AppointmentCreateView.as_view(), name='create_appointment'),
    path('appointments/update/<int:pk>', views.AppointmentUpdateView.as_view(), name='update_appointment'),
    path('appointments/delete/<int:pk>', views.AppointmentDeleteView.as_view(), name='delete_appointment'),
]

handler403 = "scheduling.views.custom_permission_denied_view"