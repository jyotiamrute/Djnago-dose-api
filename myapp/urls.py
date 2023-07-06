from django.urls import path
from .views import *
urlpatterns = [
    path('machines/', MachineListCreateView.as_view(), name='machine-list-create'),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('doses/', DoseListCreateView.as_view(), name='dose-list-create'),
    # path('machines/<uuid:pk>/', MachineGetUpdateDeleteView.as_view(), name='machine-get-update-destroy'),
    # path('patients/<uuid:pk>/', PatientGetUpdateDeleteView.as_view(), name='patient-get-update-destroy'),
    # path('doses/<int:pk>/', DoseGetUpdateDeleteView.as_view(), name='dose-get-update-destroy'),
    
    
    # this  api endpoint help  to retrieves the last dose for a given machine_id
    path('last-dose/<uuid:machine_id>/', LastDoseByMachineView.as_view(), name='last-dose-by-machine'),
]
