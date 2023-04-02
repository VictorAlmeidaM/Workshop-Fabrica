from rest_framework import serializers
from .models import Paciente, Medico, Dentista

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['nome','telefone']

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['nome','telefone','codigo']

class DentistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dentista
        fields = ['nome','telefone','codigo']
