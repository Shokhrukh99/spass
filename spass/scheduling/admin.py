from django.contrib import admin
from .models import *

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'doctor', 'patient', 'service', 'status')
    search_fields = ('doctor__name', 'patient__name', 'service__name')
    list_filter = ('service', 'start_time')
    ordering = ('-start_time',)

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'phone_number')
    search_fields = ('name',)
    list_filter = ('specialization',)
    inlines = [AppointmentInline]

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'phone_number')
    search_fields = ('name',)
    list_filter = ('dob',)
    inlines = [AppointmentInline]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
