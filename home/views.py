from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from admin_material.forms import RegistrationForm

from home.models import especialista
from .forms import EmpresaForm, EspecialistaForm, PessoaForm

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def register(request, perfil='paciente'):    
    
    mensagem = ""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if perfil == 'empresa':
            perfil_form = EmpresaForm(request.POST)
        elif perfil == 'especialista':
            perfil_form = EspecialistaForm(request.POST)
        else:
            perfil_form = PessoaForm(request.POST)

        if form.is_valid() and perfil_form.is_valid:
            form.save()
            perfil_form.save()
            print('Conta criada com sucesso!')
            return redirect('/accounts/login/')
        else:
            mensagem = "Cadastro não realizado!"
            print("Cadastro não realizado!")
    else:
        form    = RegistrationForm()
        if perfil == 'empresa':
            perfil_form = EmpresaForm()
        elif perfil == 'especialista':
            perfil_form = EspecialistaForm()
        else:
            perfil_form = PessoaForm()

    context = { 'form': form, 
                'perfil':perfil, 
                'perfil_form': perfil_form,
                'msg': mensagem }    
    return render(request, 'accounts/register.html', context)

def dashboard(request):
    # Page from the theme 
    return render(request, 'pages/index.html')
