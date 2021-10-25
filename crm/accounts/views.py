from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def rotinas(request):
    return render(request, 'accounts/rotinas.html')


def treinamento(request):
    return render(request, 'accounts/treinamento.html')


def costumer(request):
    return render(request, 'accounts/costumer.html')
