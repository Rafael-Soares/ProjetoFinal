from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html' )

'''
POSSÍVEIS FUNÇÕES DE VIEWS A SEREM IMPLEMENTADAS

def login():
def cadastro():
def perfil():
def aula():
def simulado():
def materiais():
def recuperar_senha():
    
'''