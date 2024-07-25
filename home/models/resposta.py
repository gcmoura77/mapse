from django.db import models

from .timestampedmodel import TimeStampedModel
from django.contrib.auth.models import User
from .questionario import OpcaoEscolha, Questionario
from .codigo_ativacao import CodigoAtivacao
from .mapeamento import Mapeamento

class Resposta(TimeStampedModel):                                
    
    class SituacaoResposta(models.IntegerChoices):
        Pendente = 0, "Pendente"
        Respondido = 1, "Respondido"
        Incompleto = 2, "Incompleto"
        Cancelado = 3, "Cancelado"

    questionario    = models.ForeignKey(Questionario, on_delete=models.PROTECT)
    respostas       = models.ManyToManyField(OpcaoEscolha)
    data_resposta   = models.DateTimeField(auto_now_add=True)
    situacao        = models.IntegerField(choices=SituacaoResposta.choices, default=SituacaoResposta.Pendente)
    participante    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    mapeamento      = models.ForeignKey(Mapeamento, on_delete=models.PROTECT, null=True, blank=True)
    codigo_ativacao = models.ForeignKey(CodigoAtivacao, on_delete=models.PROTECT, null=True, blank=True)


