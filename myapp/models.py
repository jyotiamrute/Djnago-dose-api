from django.db import models
import uuid
# Create your models here.

class Machine(models.Model):#Machine model class 
    machine_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine_name = models.CharField(max_length=255)

class Patient(models.Model):#Patient model class
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=255)

class Dose(models.Model):#Dose model class
    dose_id = models.AutoField(primary_key=True)
    dose = models.FloatField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
