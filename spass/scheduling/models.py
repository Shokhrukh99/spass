from django.db.models import Model, CharField, EmailField, DateField

# Create your models here.
class Doctor(Model):
    name = CharField(max_length=100)
    email = EmailField(unique=True)
    specialization = CharField(max_length=100)
    phone_number = CharField(max_length=15)

    def __str__(self):
        return f'{self.name} - {self.specialization}'

class Patient(Model):
    name = CharField(max_length=100)
    email = EmailField(unique=True)
    dob = DateField()
    phone_number = CharField(max_length=15)

    def __str__(self):
        return f'{self.name} - {self.dob}'