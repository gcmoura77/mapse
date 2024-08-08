from django import forms
from zmq import NULL

from home.models import Empresa, Pessoa, Especialista, Perfil

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
