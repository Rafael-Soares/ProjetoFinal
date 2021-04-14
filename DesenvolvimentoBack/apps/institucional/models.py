from django.db import models
from datetime import datetime
   
class home(models.Model): 
    quantidade_parcelas = models.IntegerField('Quantidade de Parcelas', default=0)
    preco_card = models.FloatField('Preço do Card', default=0)
    descricao_card = models.TextField('Descrição do Card', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class quemSomos(models.Model):
    oferecimento = models.TextField('O que oferecemos', blank=True)
    oque_fazemos = models.TextField('O que fazemos', blank=True)
    valores = models.TextField('Valores da instituição', blank=True)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)

class servicos(models.Model):
    logo_servico = models.ImageField('Logo do serviço', upload_to='imagens/', blank=True)
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
    valor_parcela = models.FloatField('Valor da parcela', default= 0)
    valor_a_vista = models.FloatField('Valor à vista', default=0)
    desconto = models.IntegerField('Porcentagem de desconto', default=0)
    data_modificacao = models.DateTimeField('Data de modificação', default=datetime.now, blank=True)
