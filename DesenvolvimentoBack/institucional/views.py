from django.shortcuts import render
from .models import quemSomos, contato

def index(request):
    quem = quemSomos.objects.all()
    cont = contato.objects.all()
    dados = { 
        'quem' : quem,
        'cont': cont
    }

    
    return render(request, 'index.html', dados)