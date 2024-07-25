from .timestampedmodel import TimeStampedModel
from .empresa import Empresa
from .questionario import Questionario
from django.db import models

class Mapeamento(TimeStampedModel):
    empresa       = models.ForeignKey(Empresa, related_name='mapeamentos_empresa', on_delete=models.CASCADE)
    descricao     = models.CharField(max_length=200, null=True, blank=True)
    data_inicio   = models.DateTimeField(null=True, blank=True)
    data_exclusao = models.DateTimeField(null=True, blank=True)
    questionarios = models.ManyToManyField(Questionario, related_name='mapeamentos_questionarios')
    
    def __str__(self):
        return str(self.empresa) + ': ' + str(self.descricao)
        
    