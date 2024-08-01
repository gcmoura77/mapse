from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout, login
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from urllib.parse import urlencode

from .models import Perfil, Empresa, Especialista, Pessoa, Questionario, CodigoAtivacao, MapeamentoAtivacao
from .forms import PerfilForm, RespostaMapeamentoForm

# Create your views here.
def index(request):
    # return render(request, 'index.html')
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home/home.html')

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
    return render(request, 'home/profile.html', context)

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
    return render(request, 'home/profile.html', context)

def get_base_template(user):
    try:
        empresa_anonimo = Empresa.objects.get(login_mapeamento=user)  # se o login esta no cadastro de empresas, significa que é um preenchimento anônimo
    except:
        empresa_anonimo = None
        
    if empresa_anonimo or not user.is_authenticated:
        base_template = "layouts/base-fullscreen.html"
    else:
        base_template = "layouts/base.html"
    
    return base_template
  
@login_required
def mapeamento(request, id):
    
    if request.method == "POST": 
        codigo = request.POST.get('codigo_ativacao')
        try:
            codigoativacao = get_object_or_404(CodigoAtivacao, codigo=codigo)
        except:
            codigoativacao = None
        post_data = request.POST
    else: 
        post_data = None
        codigo = request.GET.get('codigo_ativacao') # ao montar o questionário, precisa do código de ativação para enviar no POST
        codigoativacao = None 
        
    questionario = get_object_or_404(Questionario, pk=id)
    form = RespostaMapeamentoForm(questionario, codigoativacao, request.user, post_data)

    base_template = get_base_template(request.user)
    
    if form.is_bound and form.is_valid():
        resposta = form.save()
        
        if resposta.mapeamento:
            if request.user == resposta.mapeamento.empresa.login_mapeamento: 
                logout(request)
        url = reverse("mapeamento_encerramento")
        return redirect(url)
        
    context = {
        "segment": "mapeamento",
        "questionario": questionario,
        "form": form,
        "base_template": base_template,
        "codigo_ativacao": codigo,
    }
    return render(request, 'mapeamento/mapeamento.html', context)

def mapeamento_empresa(request):
    
    codigo_ativacao = request.POST.get('codigo_ativacao')
    questionario    = request.POST.get('escolhaQuestionario')
    
    if request.method == 'POST':
        
        if codigo_ativacao and questionario:
            codigo = CodigoAtivacao.objects.get(codigo=codigo_ativacao)
            mapeamento = MapeamentoAtivacao.objects.get(codigo_ativacao=codigo).mapeamento
            
            if not request.user.is_authenticated:
                user = mapeamento.empresa.login_mapeamento
                if user and user.is_active:
                    login(request, user)   
                else:
                    raise PermissionDenied()
                
            parameters = {
                'codigo_ativacao': codigo_ativacao,
            }
            query = urlencode(parameters)
            redirect_url = reverse('mapeamento',  kwargs={'id':questionario})
            redirect_url_with_parameters = f'{redirect_url}?{query}'    
 
            return redirect(redirect_url_with_parameters)
    
    context = {
        "segment": "Mapeamento Empresa",
    }
    return render(request, 'mapeamento/mapeamento_empresa.html', context)

def lista_questionarios(request):
    template_name = 'mapeamento/lista_questionarios_empresa.html'    
    nome_empresa = 'Não localizada'
    questionarios = {}
    codigo_ativacao = request.POST.get('codigo_ativacao')   
    try:
        codigo = CodigoAtivacao.objects.get(codigo=codigo_ativacao)
        mapeamento = MapeamentoAtivacao.objects.get(codigo_ativacao=codigo).mapeamento
        nome_empresa = mapeamento.empresa
        
        if mapeamento.empresa.login_mapeamento:        
            questionarios = mapeamento.questionarios.all()      
        else:
            messages.add_message(request, messages.WARNING, 'Empresa não está liberada para realizar o mapeamento.')                           
        
    except:
        nome_empresa = 'Código de Ativação não identificado'
        messages.add_message(request, messages.WARNING, 'Por gentileza confira se o código de ativação informado está correto')                           
     
    context = {
        "empresa": nome_empresa,
        "questionarios": questionarios,
    }
    
    return render(request, template_name, context)

def confirmacao_questionario(request):
    template_name = 'mapeamento/confirmacao_questionario.html'
    questionario = get_object_or_404(Questionario, pk=request.POST.get('escolhaQuestionario'))
    
    context = { 
        "nome_questionario_selecionado": questionario.nome,
        "total_questoes": questionario.questao_set.count(), # type: ignore
    }

    return render(request, template_name, context)

def mapeamento_encerramento(request):
    template_name = 'mapeamento/mapeamento_final.html'

    base_template = get_base_template(request.user)

    context = {
        "segment": "mapeamento",
        "base_template": base_template,
    }
    
    return render(request,template_name, context)