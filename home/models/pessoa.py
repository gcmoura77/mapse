from django.db import models
from .abstract import PessoaBaseModel

class Pessoa(PessoaBaseModel): 
    
    titulo = models.CharField(max_length=50, null=True, blank=True)
    
    @property
    def nome(self):
        return self.perfil.nome # type: ignore

    def __str__(self):
        return self.nome  # type: ignore
    
    