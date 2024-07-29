from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    # páginas de exemplo do material kit
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('billing/', views.billing, name='billing'),
    path('tables/', views.tables, name='tables'),
    path('notification/', views.notification, name='notification'),
    path('profile/', views.profile, name='profile'),
    path('typography/', views.typography, name='typography'),
    path('index/', views.index, name='index'),
]


    