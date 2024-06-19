from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Pessoa, Especialista, Empresa

# admin.site.register(Pessoa)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'login')    
    
class PessoaInline(admin.StackedInline):
    model = Pessoa
    can_delete = False
    verbose_name_plural = "pessoas"    

@admin.register(Especialista)
class EspecialistaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'conselho_profissional', 'login')
    
class EspecialistaInline(admin.StackedInline):
    model = Especialista
    can_delete = False
    verbose_name_plural = "especialistas"       

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj', 'email', 'login')
    
class EmpresaInline(admin.StackedInline):
    model = Empresa
    can_delete = False
    verbose_name_plural = "empresas"    
    
# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [PessoaInline, EspecialistaInline, EmpresaInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)