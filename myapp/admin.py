from django.contrib import admin
from .models import Machine, Patient, Dose

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_id', 'machine_name']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['patient_id', 'machine', 'patient_name']

@admin.register(Dose)
class DoseAdmin(admin.ModelAdmin):
    list_display = ['dose_id', 'dose', 'patient']
