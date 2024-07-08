from django.db import models
from .timestampedmodel import TimeStampedModel
from .questionario import OpcaoEscolha, Questionario
from .pessoa import Pessoa

class Resposta(TimeStampedModel):                                
    
    class SituacaoResposta(models.IntegerChoices):
        Pendente = 0, "Pendente"
        Respondido = 1, "Respondido"
        Incompleto = 2, "Incompleto"
        Cancelado = 3, "Cancelado"

    questionario  = models.ForeignKey(Questionario, on_delete=models.PROTECT)
    resposta      = models.ManyToManyField(OpcaoEscolha)
    data_resposta = models.DateTimeField(auto_now_add=True)
    situacao      = models.IntegerField(choices=SituacaoResposta.choices, default=SituacaoResposta.Pendente)
    pessoa        = models.ForeignKey(Pessoa, null=True, blank=True, on_delete=models.PROTECT)

