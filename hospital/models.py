from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Dentista(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    codigo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


# Create your models here.
