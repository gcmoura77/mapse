
from .abstract import PessoaBaseModel

class Pessoa(PessoaBaseModel): 
    
    @property
    def nome(self):
        return self.perfil.nome # type: ignore

    def __str__(self):
        return self.nome  # type: ignore
    
    