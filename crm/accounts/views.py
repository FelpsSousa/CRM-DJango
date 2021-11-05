from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
    return render(request, 'accounts/dashboard.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def tempo_real(request):
    return render(request, 'accounts/tempo_real.html')


def rotinas(request):
    return render(request, 'accounts/rotinas.html')


def treinamento(request):
    return render(request, 'accounts/treinamento.html')


def usuarios(request):
    usuarios = User.objects.all()
    total_usuarios = usuarios.count()

    context = {'usuarios': usuarios, 'total_usuarios': total_usuarios}

    return render(request, 'accounts/users.html', context)


def usuario(request, pk_test):
    usuarios = User.objects.all()
    usuario = User.objects.get(id=pk_test)
    total_usuarios = usuarios.count()
    qtd_felipe = usuarios.filter(nome='Felipe').count()
    avisos = usuario.aviso_set.all()
    avisos_cont = avisos.count()

    context = {'usuarios': usuarios, 'total_usuarios': total_usuarios,
               'qtd_felipe': qtd_felipe, 'usuario': usuario, 'avisos': avisos, 'avisos_cont': avisos_cont}

    return render(request, 'accounts/usuario.html', context)
