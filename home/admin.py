from tabnanny import verbose
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Pessoa, Especialista, Empresa, Perfil

# admin.site.register(Pessoa)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'cpf')    
  
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login', 'tipo_perfil', 'created', 'modified')


@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('perfil', 'cpf', 'conselho_profissional')

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('perfil','razao_social', 'cnpj')
        
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