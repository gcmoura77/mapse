from django.db import models
from django.contrib.auth.models import User

class Especialista(models.Model):                                
    nome                  = models.CharField(max_length=200)   
    cpf                   = models.CharField(max_length=11)   
    email                 = models.EmailField(null=True)
    data_nascimento       = models.DateField(null=True)                 
    conselho_profissional = models.CharField(max_length=10)
    numero_conselho       = models.BigIntegerField()
    login                 = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)        

    def __str__(self):
        return self.nome