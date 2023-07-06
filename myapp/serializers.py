from rest_framework import serializers
from .models import *


#Create a serializer for the Dose model:
class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = '__all__'

# Create a serializer for the Machine model:
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

        
# Create a serializer for the Patient model:
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


