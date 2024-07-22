from .timestampedmodel import TimeStampedModel
from .codigo_ativacao import CodigoAtivacao
from .mapeamento import Mapeamento
from django.db import models

class MapeamentoAtivacao(TimeStampedModel):  
    mapeamento      = models.ForeignKey(Mapeamento, on_delete=models.CASCADE)
    codigo_ativacao = models.OneToOneField(CodigoAtivacao, on_delete=models.CASCADE)
    usado           = models.BooleanField()
    unico           = models.BooleanField()
    
    def __str__(self):
        return str(self.codigo_ativacao) + ' - ' + str(self.mapeamento)