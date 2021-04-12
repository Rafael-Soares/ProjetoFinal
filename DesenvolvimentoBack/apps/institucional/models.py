from django.db import models
from datetime import datetime
   
class painel(models.Model):
    sloganPainel = models.CharField('Slogan do painel', max_length=255, blank=True)
    imagePainel = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class quemSomos(models.Model):
    titulo = models.CharField('Título', max_length=50, blank=True)
    oferecimento = models.TextField('O que oferecemos', blank=True)
    oque_fazemos = models.TextField('O que fazemos', blank=True)
    valores = models.TextField('Valores', blank=True)
    #não teremos imagens em quem somos imageQuemSomos = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class servicos(models.Model):
    nome = models.CharField('Nome do serviço', max_length=50, blank=True)
    #pelo mokup, n trabalharemos com imagens aqui, imageServico = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    descrição_do_servico = models.TextField('Descrição', blank=True)
    preço = models.IntegerField('Preço', default=0, blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class portifolio(models.Model):
    imagePortifolio = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    nome = models.CharField('Nome do aluno', max_length=50, blank=True)
    nota = models.IntegerField('Nota', default=0, blank=True)
    descricaoPortifolio = models.TextField('Descrição', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class contato(models.Model): #não usaremos modelos
    email = models.CharField('E-mail', max_length=255, blank=True) 
    telefone = models.CharField('Telefone', max_length=12, blank=True)
    celular = models.CharField('Celular', max_length=13, blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)