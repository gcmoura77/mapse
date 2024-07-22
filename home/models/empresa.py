from django.db import models
from django.contrib.auth.models import User
from .abstract import PerfilBase
from .timestampedmodel import TimeStampedModel
from .questionario import Questionario

class Empresa(PerfilBase):  
                                  
    razao_social          = models.CharField(max_length=200)   
    cnpj                  = models.CharField(max_length=18)   
    email_contato         = models.EmailField()
    pessoa_contato        = models.CharField(max_length=200)
    login_mapeamento      = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    @property
    def nome_fantasia(self):
        return self.perfil.nome # type: ignore

    def __str__(self):
        return self.nome_fantasia
