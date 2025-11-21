from django.db.models import (Model, CharField, EmailField, DateField, TextField,OneToOneField,
                              ForeignKey, DateTimeField, TextChoices, CASCADE)
from django.contrib.auth.models import User

# Create your models here.
class Doctor(Model):
    name = CharField(max_length=100)
    email = EmailField(unique=True)
    specialization = CharField(max_length=100)
    phone_number = CharField(max_length=15)
    user = OneToOneField(User, on_delete=CASCADE, related_name='doctor_profile', blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.specialization}'

class Patient(Model):
    name = CharField(max_length=100)
    email = EmailField(unique=True)
    dob = DateField()
    phone_number = CharField(max_length=15)

    def __str__(self):
        return f'{self.name} - {self.dob}'

class Service(Model):
    name = CharField(max_length=100)
    description = TextField(blank=True)

    def __str__(self):
        return self.name

class Appointment(Model):
    class Status(TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        CANCELLED = 'cancelled', 'Cancelled'

    doctor = ForeignKey('Doctor', on_delete=CASCADE, related_name='appointments')
    patient = ForeignKey('Patient', on_delete=CASCADE, related_name='appointments')
    service = ForeignKey('Service', on_delete=CASCADE, related_name='appointments')

    status = CharField(choices=Status.choices, default=Status.PENDING)

    start_time = DateTimeField()

    notes = TextField(blank=True)