from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Patient
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def patients_list(request):
    # Query data
    patients = Patient.objects.all()
    # Create context
    context = {
        "patients": patients
    }
    # Pass context and render template
    return render(request, 'patients.html', context)

def doctors_list(request):
    # Query data
    doctors = Doctor.objects.all()
    # Create context
    context = {
        "doctors": doctors
    }
    # Pass context and render template
    return render(request, 'doctors.html', context)

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
    else:
        form = PatientForm()
    
    return render(request, 'create_patient.html', {'form': form})

def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patients')
    return render(request, 'update_patient.html', {'form': form})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == "POST":
        patient.delete()
        return redirect('patients')
    
    return render(request, 'delete_patient.html', {'patient': patient})

def create_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
    
    return render(request, 'create_doctor.html', {'form': form})

def update_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctors')
    return render(request, 'update_doctor.html', {'form': form})

def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctors')
    
    return render(request, 'delete_doctor.html', {'doctor': doctor})