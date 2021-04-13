from django.shortcuts import render
from .models import * #esse asteristíco importa todas as classes do models

#RECUPERANDO VALORES DAS MODELS
def index(request):
    Home = home.objects.last()
    Quem_Somos = quemSomos.objects.last()
    Servico = servicos.objects.all()
    Portifolio = portifolio.objects.all()
    pacotinho = pacotes.objects.all()
    

#PASSANDO VALORES PARA UM DICIONÁRIO
    dados = { 
        'Home': Home,
        'quemSomos' : Quem_Somos,
        'servico': Servico,
        'portifolio': Portifolio,
        'paco': pacotinho
    }

    return render(request, 'index.html', dados)