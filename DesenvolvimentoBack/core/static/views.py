from django.shortcuts import render
from .models import * #esse asteristíco importa todas as classes do models

#RECUPERANDO VALORES DAS MODELS
def index(request):
    var_QuemSomos = quemSomos.objects.last()
    var_Contato = contato.objects.all()
    var_Servico = servicos.objects.all()
    var_Portifolio = portifolio.objects.all()
    var_RedesSociais = redesSociais.objects.all()
    var_Painel = painel.objects.all()

#PASSANDO VALORES PARA UM DICIONÁRIO
    dados = { 
        'quemSomos' : var_QuemSomos,
        'contato': var_Contato,
        'servico': var_Servico,
        'portifolio': var_Portifolio,
        'redesSociais': var_RedesSociais,
        'painel': var_Painel
    }

    return render(request, 'index.html', dados)