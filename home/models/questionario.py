from django.db import models
from .timestampedmodel import TimeStampedModel

class Questionario(TimeStampedModel):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1000, null=True, blank=True)      

    def __str__(self):
        return self.nome

class Questao(TimeStampedModel):
    questionario = models.ForeignKey(Questionario, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Questões"    

    def __str__(self):
        return self.descricao

class OpcaoEscolha(TimeStampedModel):
  questao = models.ForeignKey(Questao, null=True, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.questao}:{self.descricao}"