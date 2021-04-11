from django.shortcuts import render
from .models import * #esse asteristíco importa todas as classes do models

#RECUPERANDO VALORES DAS MODELS
def index(request):
    Quem_Somos = quemSomos.objects.last()
    Contato = contato.objects.all()
    Servico = servicos.objects.all()
    Portifolio = portifolio.objects.all()
    Painel = painel.objects.all()

#PASSANDO VALORES PARA UM DICIONÁRIO
    dados = { 
        'quemSomos' : Quem_Somos,
        'contato': Contato,
        'servico': Servico,
        'portifolio': Portifolio,
        'painel': Painel
    }

    return render(request, 'index.html', dados)