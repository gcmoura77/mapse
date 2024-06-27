from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from admin_material.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView,  PasswordChangeView
from django.contrib.auth import logout

from .models import Perfil, Empresa, Especialista, Pessoa
from .forms import EmpresaForm, EspecialistaForm, PessoaForm, PerfilForm

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def register(request, perfil='paciente'):    
    
    mensagem = ""
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        base_perfil_form = PerfilForm(request.POST)
        if perfil == 'empresa':
            perfil_form = EmpresaForm(request.POST)
        elif perfil == 'especialista':
            perfil_form = EspecialistaForm(request.POST)
        else:
            perfil_form = PessoaForm(request.POST)

        if all([reg_form.is_valid(), base_perfil_form.is_valid(), perfil_form.is_valid]):
            usuario_salvo = reg_form.save()
            base_perfil_salvo = base_perfil_form.save(commit=False)
            base_perfil_salvo.tipo_perfil = perfil.capitalize()
            base_perfil_salvo.login = usuario_salvo
            base_perfil_salvo.save()
            perfil_salvo = perfil_form.save(commit=False)
            perfil_salvo.perfil = base_perfil_salvo
            perfil_salvo.email_contato = usuario_salvo.email
            perfil_salvo.save()
            print('Conta criada com sucesso!')
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('/')
        else:
            mensagem = "Cadastro não realizado!"
            print("Cadastro não realizado!")
    else:
        reg_form = RegistrationForm()
        base_perfil_form = PerfilForm()
        if perfil == 'empresa':
            perfil_form = EmpresaForm()
        elif perfil == 'especialista':
            perfil_form = EspecialistaForm()
        else:
            perfil_form = PessoaForm()

    context = { 'form': reg_form, 
                'perfil':perfil, 
                'base_perfil_form': base_perfil_form,
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
    perfil = Perfil.objects.get(login = request.user)
    if perfil.tipo_perfil == 'Empresa':
        perfil_especifico = Empresa.objects.get(perfil=perfil)
        subtitulo = perfil_especifico.razao_social
    elif perfil.tipo_perfil == 'Pessoa':
        perfil_especifico = Pessoa.objects.get(perfil=perfil)
        subtitulo = perfil_especifico.titulo
    else:
        perfil_especifico = Especialista.objects.get(perfil=perfil)
        subtitulo = f'{perfil_especifico.conselho_profissional} {str(perfil_especifico.numero_conselho)}'

    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()    
            return redirect('profile/')
    
    if perfil.imagem:
        imagem_perfil = perfil.imagem.url
    else:
        imagem_perfil = ''
    

    
    context = { 'segment': 'perfil',
                'tipo_perfil': perfil.tipo_perfil, 
                'nome': perfil.nome, 
                'celular': perfil_especifico.celular,
                'email_contato': perfil_especifico.email_contato,
                'cidade': perfil_especifico.cidade,
                'facebook': perfil_especifico.facebook,
                'x_twitter': perfil_especifico.x_twitter,
                'instagram': perfil_especifico.instagram,
                'descricao': perfil.descricao,
                'subtitulo': subtitulo,
                'imageURL': imagem_perfil,
            }
    return render(request, 'profile.html', context)

@login_required
def profile_edit(request):
    context = { 'segment': 'perfil',
            'tipo_perfil': 'perfil.tipo_perfil', 
            'nome': 'edicao', 
            'celular': 'celuar',
            'e_mail': 'perfil_especifico.email_contato',
            'cidade': 'perfil_especifico.cidade',
            'facebook': 'perfil_especifico.facebook',
            'x_twitter': 'perfil_especifico.x_twitter',
            'instagram': 'perfil_especifico.instagram',
            'descricao': 'perfil.descricao',
            'subtitulo': 'subtitulo',
        }
    return render(request, 'profile.html', context)


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
  
