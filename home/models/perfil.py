from django.db import models
from django.contrib.auth.models import User
from .timestampedmodel import TimeStampedModel

class Perfil(TimeStampedModel):                                

    class Role(models.TextChoices):
        Pessoa = "Pessoa", "Pessoa"
        Especialista = "Especialista", "Especialista"
        Empresa = "Empresa", "Empresa"
    
    tipo_perfil = models.CharField(max_length=50, choices=Role.choices, default=Role.Pessoa)
    nome        = models.CharField(max_length=200)   
    login       = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome