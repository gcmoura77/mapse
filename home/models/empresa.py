from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):                                
    razao_social          = models.CharField(max_length=200)
    nome_fantasia         = models.CharField(max_length=200)   
    cnpj                  = models.CharField(max_length=14)   
    email                 = models.EmailField()
    pessoa_contato        = models.CharField(max_length=200)                 
    login                 = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)        

    def __str__(self):
        return self.nome_fantasia