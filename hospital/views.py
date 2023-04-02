from rest_framework import viewsets
from .serializer import PacienteSerializer, MedicoSerializer, DentistaSerializer
from .models import Paciente, Medico, Dentista

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class DentistaViewSet(viewsets.ModelViewSet):
    queryset = Dentista.objects.all()
    serializer_class = DentistaSerializer