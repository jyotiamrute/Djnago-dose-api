from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import Http404

# here created a view class that retrieves the last dose for a given machine_id
class LastDoseByMachineView(APIView): #Class to get last dose by machine id
    def get_last_dose(self, machine_id):
        try:
            machine = Machine.objects.get(machine_id=machine_id)
            patient = machine.patient_set.last()
            if patient:
                dose = patient.dose_set.last()
                return dose
            return None
        except (Machine.DoesNotExist, Patient.DoesNotExist, Dose.DoesNotExist):
            raise Http404

    def get(self, request, machine_id):
        try:
            dose = self.get_last_dose(machine_id)
            if dose:
                response_data = {
                    "Machine_id": dose.patient.machine.machine_id,
                    "Patient_id": dose.patient.patient_id,
                    "Patient_name": dose.patient.patient_name,
                    "Dose_id": dose.dose_id,
                    "Dose": dose.dose
                }
                return Response(response_data)
            else:
                return Response({"detail": "No dose found for the machine"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MachineListCreateView(APIView):#Class to create Machine list
    def get(self, request):#get all machines
        try:
            machines = Machine.objects.all()
            serializer = MachineSerializer(machines, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = MachineSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PatientListCreateView(APIView):# Class to create Patients list
    def get(self, request):#get all patients
        try:
            patients = Patient.objects.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DoseListCreateView(APIView):#Class to create Doses list
    def get(self, request):#get all doses
        try:
            doses = Dose.objects.all()
            serializer = DoseSerializer(doses, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = DoseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







#retrive update delete the machine using id
class MachineGetUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Machine.objects.get(pk=pk)
        except Machine.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            machine = self.get_object(pk)
            serializer = MachineSerializer(machine)
            return Response(serializer.data)
        except Machine.DoesNotExist:
            return Response({"detail": "Machine not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            machine = self.get_object(pk)
            serializer = MachineSerializer(machine, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Machine.DoesNotExist:
            return Response({"detail": "Machine not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            machine = self.get_object(pk)
            machine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Machine.DoesNotExist:
            return Response({"detail": "Machine not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#retrive update delete the Patient using id
class PatientGetUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            patient = self.get_object(pk)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        except Patient.DoesNotExist:
            return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            patient = self.get_object(pk)
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Patient.DoesNotExist:
            return Response({"detail": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#retrive update delete the Doses using id
class DoseGetUpdateDeleteView(APIView):
    def get_object(self, pk):
        try:
            return Dose.objects.get(pk=pk)
        except Dose.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            dose = self.get_object(pk)
            serializer = DoseSerializer(dose)
            return Response(serializer.data)
        except Dose.DoesNotExist:
            return Response({"detail": "Dose not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            dose = self.get_object(pk)
            serializer = DoseSerializer(dose, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Dose.DoesNotExist:
            return Response({"detail": "Dose not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            dose = self.get_object(pk)
            dose.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Dose.DoesNotExist:
            return Response({"detail": "Dose not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
