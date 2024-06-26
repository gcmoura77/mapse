from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):                                
    nome             = models.CharField(max_length=200)   
    cpf              = models.CharField(max_length=14, blank=True)   
    email            = models.EmailField()
    data_nascimento  = models.DateField()     
    login            = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome