from django.db import models
from .abstract import PerfilBase

class Empresa(PerfilBase):  
                                  
    razao_social          = models.CharField(max_length=200)   
    cnpj                  = models.CharField(max_length=18)   
    email_contato         = models.EmailField()
    pessoa_contato        = models.CharField(max_length=200)                 
    
    @property
    def nome_fantasia(self):
        return self.perfil.nome # type: ignore

    def __str__(self):
        return self.nome_fantasia
    
    