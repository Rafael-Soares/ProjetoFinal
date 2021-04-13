from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FormContato
from .models import * #esse asteristíco importa todas as classes do models

#RECUPERANDO VALORES DAS MODELS
def index(request):
    Home = home.objects.last()
    Quem_Somos = quemSomos.objects.last()
    Servico = servicos.objects.all()
    Portifolio = portifolio.objects.all()
    pacotinho = pacotes.objects.all()

    context = {}

    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            context['is_valid'] = True #PODE TIRAR
            form.send_mail()
            form = FormContato()
    else:
        form = FormContato()

#PASSANDO VALORES PARA UM DICIONÁRIO
    context = { 
        'Home': Home,
        'quemSomos' : Quem_Somos,
        'servico': Servico,
        'portifolio': Portifolio,
        'paco': pacotinho,
        'form': form
    }

    return render(request, 'index.html', context)