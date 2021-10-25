from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('rotinas/', views.rotinas),
    path('treinamento/', views.treinamento),
    path('costumer/', views.costumer),
]
