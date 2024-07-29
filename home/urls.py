from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),     
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('mapeamento/<int:id>/', views.mapeamento,name='mapeamento'),
    path('mapeamento/empresa/', views.mapeamento_empresa,name='mapeamento_empresa'),
    path('mapeamento/lista_questionarios/', views.lista_questionarios, name='lista_questionarios'),
    path('mapeamento/confirmacao_questionario/', views.confirmacao_questionario, name='confirmacao_questionario'),
    path('mapeamento/mapeamento_encerramento/', views.mapeamento_encerramento, name='mapeamento_encerramento'),
    
    # páginas de autenticação
    path("accounts/register/<str:perfil>/", views.register, name='register'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    