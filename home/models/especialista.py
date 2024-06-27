from django.db import models

from home.models.perfil import Perfil
from .abstract import PessoaBaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver


class Especialista(PessoaBaseModel):                                

    conselho_profissional = models.CharField(max_length=10)
    numero_conselho       = models.BigIntegerField()

    @property
    def nome(self):
        if self.perfil:
            return self.perfil.nome # type: ignore
        else:
            return 'sem perfil'

    def __str__(self):
        return self.nome  
    

