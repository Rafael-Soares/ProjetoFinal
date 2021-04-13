from django.db import models
from datetime import datetime
   
class home(models.Model):
    slogan_home = models.CharField('Slogan do Home', max_length=255, blank=True)
    imageHome = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    descricao_card = models.TextField('Descrição do Card', blank=True) 
    preco_card = models.IntegerField('Preço do Card', default=0)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class quemSomos(models.Model):
    titulo = models.CharField('Título', max_length=50, blank=True)
    oferecimento = models.TextField('O que oferecemos', blank=True)
    oque_fazemos = models.TextField('O que fazemos', blank=True)
    valores = models.TextField('Valores da instituição', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class servicos(models.Model):
    nome = models.CharField('Nome do serviço', max_length=50, blank=True)
    descrição_do_servico = models.TextField('Descrição', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class portifolio(models.Model):
    imagePortifolio = models.ImageField('Imagem', upload_to='imagens/', blank=True)
    nome = models.CharField('Nome do aluno', max_length=50, blank=True)
    nota = models.IntegerField('Nota', default=0, blank=True)
    descricaoPortifolio = models.TextField('Descrição', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class pacotes(models.Model):
    duracao_pacote = models.CharField('Duração do Pacote', max_length=30)
    quantidade_parcelas = models.IntegerField('Quantidade de parcelas', default=0)
    #tem q ser uma variável float valor_parcela = 
    desconto = models.IntegerField('Porcentagem de desconto', default=0)
    atributos_pacote = models.TextField('Atributos do pacote', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

#class contato(models.Model): #não usaremos modelos
#    email = models.CharField('E-mail', max_length=255, blank=True) 
#   telefone = models.CharField('Telefone', max_length=12, blank=True)
#    celular = models.CharField('Celular', max_length=13, blank=True)
#    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)