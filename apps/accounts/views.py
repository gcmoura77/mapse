from django.shortcuts import render, redirect
from admin_material.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView,  PasswordChangeView
from django.contrib.auth import logout
from .forms import EmpresaForm, EspecialistaForm, PessoaForm, PerfilForm

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
