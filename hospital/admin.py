from django.contrib import admin
from .models import Paciente, Medico, Dentista

# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone')

admin.site.register(Paciente,PacientesAdmin)

class MedicosAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','codigo')

admin.site.register(Medico,MedicosAdmin)

class DentistasAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','codigo')

admin.site.register(Dentista,DentistasAdmin)