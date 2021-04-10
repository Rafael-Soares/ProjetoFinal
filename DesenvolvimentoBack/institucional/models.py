
from django.db import models
from datetime import datetime
   
class painel(models.Model):
    sloganPainel = models.CharField('Slogan do painel', max_length=255)
    imagePainel = models.ImageField('Imagem', upload_to='imagens/', blank=True)

class quemSomos(models.Model):
    titulo = models.CharField('Título', max_length=50)
    apresentacao = models.TextField('Apresentação')
    imageQuemSomos = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class servicos(models.Model):
    nome = models.CharField('Nome do serviço', max_length=50)
    imageServico = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    descrição_do_servico = models.TextField('Descrição')
    preço = models.CharField('Preço', max_length=13)

class portifolio(models.Model):
    descricaoPortifolio = models.TextField('Descrição')
    imagePortifolio = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    preco = models.IntegerField()

class contato(models.Model): #não usaremos modelos
    email = models.CharField('E-mail', max_length=255) 
    telefone = models.CharField('Telefone', max_length=12)
    celular = models.CharField('Celular', max_length=13)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)


class redesSociais(models.Model):
    nomeRS = models.CharField('Nome na rede', max_length=30)
    link = models.CharField('Link de aceeso à rede', max_length=100)