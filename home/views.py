from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from admin_material.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordResetView,  PasswordChangeView
from django.contrib.auth import logout, authenticate, login
from django.core.exceptions import PermissionDenied
import os

from .models import Perfil, Empresa, Especialista, Pessoa, Questionario, CodigoAtivacao
from .forms import EmpresaForm, EspecialistaForm, PessoaForm, PerfilForm, QuestionarioForm

from django.urls import reverse

# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def register(request, perfil='pessoa'):    
    
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
            print('Cadastro não realizado!')
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
        imagem_perfil = '/static/img/perfil-no-fundo-branco-vetor.jpg'
        
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
  
@login_required
def mapeamento(request, id):
    questionario = get_object_or_404(Questionario, pk=id)
    post_data = request.POST if request.method == "POST" else None
    form = QuestionarioForm(questionario, post_data)

    try:
        empresa = Empresa.objects.get(login_mapeamento=request.user)
        base_template = "layouts/base-fullscreen.html"
    except:
        # esta parte ainda precisa ser pensada, no caso do preenchimento individual identificado pelo login da pessoa
        empresa = {}
        base_template = "layouts/base.html"

    
    url = reverse("mapeamento", args=[id])
    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Envio salvo.')
        return redirect(url)
        
    context = {
        "segment": "mapeamento",
        "questionario": questionario,
        "form": form,
        "empresa": empresa,
        "base_template": base_template,
    }
    return render(request, 'mapeamento.html', context)

def mapeamento_empresa(request):
    
    codigo_ativacao = request.POST.get('codigo_empresa')
    questionario    = request.POST.get('escolhaQuestionario')
    
    if request.method == 'POST':
        
        if codigo_ativacao and questionario:
            codigo = CodigoAtivacao.objects.get(codigo=int(codigo_ativacao))
            if not request.user.is_authenticated:
                user = codigo.empresa.login_mapeamento
                if user and user.is_active:
                    login(request, user)    
                else:
                    raise PermissionDenied()
            return redirect('mapeamento', id=questionario)
    
    context = {
        "segment": "Mapeamento Empresa",
    }
    return render(request, 'mapeamento_empresa.html', context)

def lista_questionarios(request):
    template_name = 'partials/lista_questionarios_empresa.html'    
    nome_empresa = 'Não localizada'
    questionarios = {}
    
    codigo_ativacao = request.POST.get('codigo_empresa')   
    
    try:
        codigo = CodigoAtivacao.objects.get(codigo=int(codigo_ativacao))
        nome_empresa = codigo.empresa
        questionarios = codigo.empresa.questionarios.all()      # type: ignore
    except:
        nome_empresa = 'Código de Ativação não identificado'  
     
    context = {
        "empresa": nome_empresa,
        "questionarios": questionarios,
    }
    
    return render(request, template_name, context)

def confirmacao_questionario(request):
    template_name = 'partials/confirmacao_questionario.html'
    questionario = get_object_or_404(Questionario, pk=request.POST.get('escolhaQuestionario'))
    
    context = { 
        "nome_questionario_selecionado": questionario.nome,
        "total_questoes": questionario.questao_set.count(), # type: ignore
    }

    return render(request, template_name, context)