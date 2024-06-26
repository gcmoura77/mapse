from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from admin_material.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView,  PasswordChangeView
from django.contrib.auth import logout

from home.admin import EspecialistaAdmin

from .models import Pessoa, Empresa, Especialista
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

        if all([form.is_valid(),  perfil_form.is_valid]):
            usuario_salvo = form.save()
            perfil_salvo = perfil_form.save(commit=False)
            perfil_salvo.login = usuario_salvo
            perfil_salvo.email = usuario_salvo.email
            perfil_salvo.save()
            print('Conta criada com sucesso!')
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('/')
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

@login_required
def dashboard(request):
    # Page from the theme 
    return render(request, 'pages/index.html')

@login_required
def billing(request):
  return render(request, 'pages/billing.html', { 'segment': 'billing' })

@login_required
def tables(request):
  return render(request, 'pages/tables.html', { 'segment': 'tables' })

@login_required
def notification(request):
  return render(request, 'pages/notifications.html', { 'segment': 'notification' })

@login_required
def profile(request):
  
  pessoa = Pessoa.objects.get(login = request.user)
  if pessoa:
    tipo_perfil = 'pessoa'
    nome = pessoa.nome    
  else:
    empresa = Empresa.objects.get(login = request.user)
    if empresa:
      tipo_perfil = 'empresa'
      nome = empresa.razao_social
    else:
      especialista = Especialista.objects.get(login = request.user)
      nome = especialista.nome
      tipo_perfil = 'especialista'
  
  return render(request, 'profile.html', { 'segment': 'perfil','tipo_perfil': tipo_perfil, 'nome': nome})


# Authentication
class UserLoginView(LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  
class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm
  
def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm
  
