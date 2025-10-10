from django.forms import ModelForm, DateInput
from .models import *
from django.core.exceptions import ValidationError

class DateInput(DateInput):
    input_type = 'date'

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'dob': DateInput()
        }
        
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if not phone.startswith("998") or len(phone) != 12:
            raise ValidationError("Phone number must be in format: 998xxxxxxxxx")
        return phone
        
class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if not phone.startswith("998") or len(phone) != 12:
            raise ValidationError("Phone number must be in format: 998xxxxxxxxx")

