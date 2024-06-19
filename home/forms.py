from django import forms
from .models import Empresa, Pessoa, Especialista

class PessoaForm(forms.ModelForm):
    
    class Meta:
        model = Pessoa
        fields =  ['nome', 'cpf','data_nascimento']
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu Nome'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CPF'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data de Nascimento',
                'type' : 'date'
            })
        }        
    
class EspecialistaForm(forms.ModelForm):
    
    class Meta:
        model = Especialista
        fields =  ['nome','cpf','data_nascimento', 'conselho_profissional', 'numero_conselho']
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu Nome'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CPF'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data de Nascimento',
                'type' : 'text',
            }),            
            'conselho_profissional': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Conselho Profissional'
            }),
            'numero_conselho': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número do Conselho'
            }),
        }        
    
class EmpresaForm(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields =  ['razao_social','cnpj','pessoa_contato']
        
        widgets = {
            'razao_social': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da Empresa'
            }),
            'cnpj': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CNPJ'
            }),
            'pessoa_contato': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Pessoa de Contato'
            }),
        }        
    