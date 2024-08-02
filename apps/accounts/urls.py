from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # páginas de autenticação
    path("register/<str:perfil>/", views.register, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('logout/', views.logout_view, name='logout'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
]


    