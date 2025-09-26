from django.shortcuts import render
from .models import Doctor, Patient

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