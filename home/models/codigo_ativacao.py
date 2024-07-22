from .timestampedmodel import TimeStampedModel
from django.db import models

class CodigoAtivacao(TimeStampedModel):  
    codigo               = models.CharField(default='ABCD1234', max_length=8, blank=True)   
    
    def __str__(self):
        return str(self.codigo)
    
