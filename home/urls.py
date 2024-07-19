from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),     
    path('home/', views.home, name='home'),
    path("accounts/register/<str:perfil>/", views.register, name='register'),
    path('accounts/register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('mapeamento/<int:id>/', views.mapeamento,name='mapeamento'),
    path('mapeamento/empresa/', views.mapeamento_empresa,name='mapeamento_empresa'),
    path('mapeamento/lista_questionarios/', views.lista_questionarios, name='lista_questionarios'),
    path('mapeamento/confirmacao_questionario/', views.confirmacao_questionario, name='confirmacao_questionario'),
    
    # páginas de autenticação
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    # páginas de exemplo do material kit
    path('dashboard/', views.dashboard, name='dashboard'), # original da bibliteca
    path('billing/', views.billing, name='billing'),
    path('tables/', views.tables, name='tables'),
    path('notification/', views.notification, name='notification'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    