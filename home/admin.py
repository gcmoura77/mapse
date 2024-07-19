from tabnanny import verbose
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from home.models.empresa import CodigoAtivacao

from .models import Pessoa, Especialista, Empresa, Perfil, Questionario, Questao, OpcaoEscolha, Resposta, QuestionarioEmpresa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'cpf')    
  
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login', 'tipo_perfil', 'created', 'modified')

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'cpf', 'conselho_profissional')


class CodigoAtivacaoInLine(admin.TabularInline):
    model = CodigoAtivacao
    show_change_link = True
    verbose_name_plural = "Códigos"    
    
class QuestionariosEmpresaInLine(admin.TabularInline):
    model = QuestionarioEmpresa
    show_change_link = True
    verbose_name_plural = "Questionários"        

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('perfil','razao_social', 'cnpj')
    inlines = [CodigoAtivacaoInLine, QuestionariosEmpresaInLine]    
        
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = "Perfis"    
  
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [PerfilInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class QuestaoInline(admin.TabularInline):
    model = Questao
    show_change_link = True
    verbose_name_plural = "Questões"    

class OpcaoEscolhaInLine(admin.TabularInline):
    model = OpcaoEscolha
    show_change_link = True
    verbose_name_plural = "Opções"    
   
@admin.register(Questionario)
class QuestionarioAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [QuestaoInline]    

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    inlines = [OpcaoEscolhaInLine]

@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ("data_resposta", "situacao", "pessoa")
    
admin.site.register(OpcaoEscolha)
