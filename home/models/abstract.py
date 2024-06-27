from django.db import models
from .perfil import Perfil
from .timestampedmodel import TimeStampedModel
      
class PerfilBase(TimeStampedModel):
   
    perfil           = models.OneToOneField(Perfil, on_delete=models.SET_NULL, null=True)
    celular          = models.CharField(max_length=20, blank=True)   
    cidade           = models.CharField(max_length=120, blank=True)
    facebook         = models.CharField(max_length=60, blank=True)
    x_twitter        = models.CharField(max_length=60, blank=True)
    instagram        = models.CharField(max_length=60, blank=True)
    
    class Meta:
        abstract = True
        
class PessoaBaseModel(PerfilBase):
    
    cpf                   = models.CharField(max_length=14)   
    email_contato         = models.EmailField(null=True)
    data_nascimento       = models.DateField(null=True)     
                
    
    class Meta:
        abstract = True
