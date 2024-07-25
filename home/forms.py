from django import forms
from zmq import NULL

from .models import Empresa, Pessoa, Especialista, Perfil
from home.models.mapeamento_ativacao import MapeamentoAtivacao
from home.models.questionario import OpcaoEscolha
from home.models.resposta import Resposta

class PerfilForm(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ('nome',)
        labels = {'nome': 'Nome',}
                
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),        
        }

class PessoaForm(forms.ModelForm):
    
    class Meta:
        model = Pessoa
        fields =  ['cpf','data_nascimento']
        labels = {'cpf': 'CPF', 'data_nascimento': 'Data Nascimento'}
        
        widgets = {
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'data-mask': '000.000.000-00',                
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control datepicker',
            })
        }        
    
class EspecialistaForm(forms.ModelForm):
    
    class Meta:
        model = Especialista
        fields =  ['cpf','data_nascimento', 'conselho_profissional', 'numero_conselho']
        labels = {'cpf': 'CPF', 
                  'data_nascimento': 'Data Nascimento',
                  'conselho_profissional': 'Conselho Profissional', 
                  'numero_conselho': 'Número do Conselho'}
        
        widgets = {
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'data-mask': '000.000.000-00',
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control datepicker',
            }),            
            'conselho_profissional': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'numero_conselho': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
        }        
    
class EmpresaForm(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields =  ['razao_social','cnpj','pessoa_contato']
        labels = {'razao_social': 'Razão Social', 
                  'cnpj': 'CNPJ',
                  'pessoa_contato': 'Pessoa de Contato'}        
        widgets = {
            'razao_social': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'data-mask': '00.000.000/0000-00',
            }),
            'pessoa_contato': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
    
class RespostaMapeamentoForm(forms.Form):

    def __init__(self, questionario, codigoativacao, participante, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.questionario = questionario
        self.codigoativacao = codigoativacao
        if codigoativacao:
            self.mapeamento = MapeamentoAtivacao.objects.get(codigo_ativacao=codigoativacao).mapeamento
            
        self.participante = participante
        for questao in questionario.questao_set.all():
            opcoesescolha = [(opcaoescolha.id, opcaoescolha.descricao) for opcaoescolha in questao.opcaoescolha_set.all()]
            self.fields[f"questao_{questao.id}"] = forms.ChoiceField(widget=forms.RadioSelect, choices=opcoesescolha)
            self.fields[f"questao_{questao.id}"].label = questao.descricao
          
    def save(self):
      data = self.cleaned_data
      resposta = Resposta(questionario=self.questionario)
      resposta.participante=self.participante
      # verificar quais as respostas que foram preenchidas se todas estiverem ok, Respondida, caso contrário Incompleto
      resposta.situacao = Resposta.SituacaoResposta.Respondido 
      
      if self.codigoativacao:
          resposta.codigo_ativacao = self.codigoativacao
          resposta.mapeamento = self.mapeamento
          
      resposta.save()
      for questao in self.questionario.questao_set.all():
          opcaoescolha = OpcaoEscolha.objects.get(pk=data[f"questao_{questao.id}"])
          resposta.respostas.add(opcaoescolha)
      
      resposta.save()
      return resposta          
  
  