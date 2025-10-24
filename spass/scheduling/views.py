from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Doctor, Patient, Service
from .forms import *
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


# --- HOME PAGE ---
def home(request):
    context={
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'service_count': Service.objects.count(),
        'appointment_count': Appointment.objects.count()
    }
    return render(request, 'home.html', context=context)


# --- LISTS PAGES ---
def patients_list(request):
    # Query data
    patients = Patient.objects.all()
    # Create context
    context = {
        "patients": patients
    }
    # Pass context and render template
    return render(request, 'patients/patients.html', context)

def doctors_list(request):
    # Query data
    doctors = Doctor.objects.all()
    # Create context
    context = {
        "doctors": doctors
    }
    # Pass context and render template
    return render(request, 'doctors/doctors.html', context)

def services_list(request):
    # Query data
    services = Service.objects.all()
    # Create context
    context = {
        "services": services
    }
    # Pass context and render template
    return render(request, 'services/services.html', context)


# --- PATIENT CRUD ---
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient was successfully added")
            return redirect('patients')
    else:
        form = PatientForm()
    
    return render(request, 'patients/create_patient.html', {'form': form})

def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        messages.info(request, "Patient successfully updated")
        return redirect('patients')
    return render(request, 'patients/update_patient.html', {'form': form})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.delete()
        messages.warning(request, "Patient deleted")
        return redirect('patients')
    
    return render(request, 'patients/delete_patient.html', {'patient': patient})


# --- DOCTOR CRUD ---
def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor was successfully added")
            return redirect('doctors')
    else:
        form = DoctorForm()
    
    return render(request, 'doctors/create_doctor.html', {'form': form})

def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        messages.info(request, "Doctor successfully updated")
        return redirect('doctors')
    return render(request, 'doctors/update_doctor.html', {'form': form})

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.delete()
        messages.warning(request, "Doctor deleted")
        return redirect('doctors')
    
    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})


# --- SERVICES CRUD ---
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "service was successfully added")
            return redirect('services')
    else:
        form = ServiceForm()
    
    return render(request, 'services/create_service.html', {'form': form})

def update_service(request, id):
    service = get_object_or_404(Service, id=id)
    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        form.save()
        messages.info(request, "service successfully updated")
        return redirect('services')
    return render(request, 'services/update_service.html', {'form': form})

def delete_service(request, id):
    service = get_object_or_404(service, id=id)
    if request.method == "POST":
        service.delete()
        messages.warning(request, "service deleted")
        return redirect('services')
    
    return render(request, 'services/delete_service.html', {'service': service})

# --- APPOINTMENT CRUD ---
class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointments/appointments.html'
    context_object_name = 'appointments'
    ordering = ['-start_time']

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/create_appointment.html'
    success_url = reverse_lazy('appointments')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/update_appointment.html'
    success_url = reverse_lazy('appointments')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointments/delete_appointment.html'
    success_url = reverse_lazy('appointments')