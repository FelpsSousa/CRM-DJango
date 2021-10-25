from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def rotinas(request):
    return render(request, 'accounts/rotinas.html')


def treinamento(request):
    return render(request, 'accounts/treinamento.html')


def custumer(request):
    return render(request, 'accounts/custumer.html')
