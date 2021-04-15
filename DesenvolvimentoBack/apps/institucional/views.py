from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FormContato
from .models import * #esse asteristíco importa todas as classes do models

#RECUPERANDO VALORES DAS MODELS
def index(request):
    Home = home.objects.last()
    Quem_Somos = quemSomos.objects.last()
    #Servico = servicos.objects.all()
    servicosAll = servicos.objects.all()[1:]
    Portifolio = portifolio.objects.all()
    pacotinho = pacotes.objects.all()
    servicos1 = servicos.objects.first()
    message = False

    id1 = Portifolio.get(id=1)
    id2 = Portifolio.get(id=2)
    id3 = Portifolio.get(id=3)

    context = {}

    if request.method == 'POST':
        form = FormContato(request.POST)
        if form.is_valid():
            message = True
            form.send_mail()
            form = FormContato()
    else:
        form = FormContato()

#PASSANDO VALORES PARA UM DICIONÁRIO
    context = { 
        'Home': Home,
        'quemSomos' : Quem_Somos,
        'servico': servicosAll,
        'servico1': servicos1,
        'portifolio': Portifolio,
        'paco': pacotinho,
        'form': form,
        'id1': id1,
        'id2': id2,
        'id3': id3,
        'mensagem': message
    }

#    for x in Portifolio:
#        if (x.id % 2 == 0):
#            context['par'] = True
#        else:
#            context['impar']  = True
  
    return render(request, 'index.html', context)

def notfound(request):
    return render(request, 'notfound.html')