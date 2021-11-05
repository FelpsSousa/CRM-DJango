from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('rotinas/', views.rotinas, name='rotinas'),
    path('treinamento/', views.treinamento, name='treinamento'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuario/<str:pk_test>/', views.usuario, name='usuario'),
    path('tempo_real/', views.tempo_real, name='tempo_real')
]
