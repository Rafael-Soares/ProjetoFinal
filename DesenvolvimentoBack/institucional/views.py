from django.shortcuts import render
from .models import quemSomos, contato, servicos, portifolio

def index(request):
    quem = quemSomos.objects.all()
    cont = contato.objects.all()
    servi = servicos.objects.all()
    portifo = portifolio.objects.all()
    dados = { 
        'quem' : quem,
        'cont': cont,
        'servi': servi,
        'portifo':portifo
    }

    return render(request, 'index.html', dados)