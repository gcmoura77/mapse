from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),     
    path('home/', views.home, name='home'),
    path("accounts/register/<str:perfil>/", views.register, name='register'),
    path('accounts/register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'), # original da bibliteca

]
