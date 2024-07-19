from django.db import models
from django.contrib.auth.models import User
from .abstract import PerfilBase
from .timestampedmodel import TimeStampedModel
from .questionario import Questionario

class Empresa(PerfilBase):  
                                  
    razao_social          = models.CharField(max_length=200)   
    cnpj                  = models.CharField(max_length=18)   
    email_contato         = models.EmailField()
    pessoa_contato        = models.CharField(max_length=200)
    login_mapeamento      = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    @property
    def nome_fantasia(self):
        return self.perfil.nome # type: ignore

    def __str__(self):
        return self.nome_fantasia
    
class CodigoAtivacao(TimeStampedModel):  
                                  
    empresa      = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    codigo       = models.IntegerField(default=888888, blank=True, primary_key=True)   
    
    def __str__(self):
        return str(self.codigo)

class QuestionarioEmpresa(TimeStampedModel):
    empresa         = models.ForeignKey(Empresa, related_name='questionarios', on_delete=models.CASCADE)
    questionario    = models.ForeignKey(Questionario, related_name='empresas', on_delete=models.CASCADE)
    data_ativacao   = models.DateTimeField(null=True, blank=True)
    data_inativacao = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return str(self.empresa) + ': ' + str(self.questionario)

    
    