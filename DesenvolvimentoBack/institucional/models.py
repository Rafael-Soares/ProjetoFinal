from django.db import models
from datetime import datetime

class quemSomos(models.Model):
    titulo = models.CharField(max_length=50)
    apresentacao = models.TextField()
    #imagem
    data_modificacao = models.DateTimeField(default=datetime.now, blank=True)

class servicos(models.Model):
    nome = models.CharField(max_length=50)
    descrição_do_servico = models.TextField()
    preço = models.CharField(max_length=13)

class portifolio(models.Model):
    descricao_port = models.TextField()

class contato(models.Model):
    email = models.CharField(max_length=255) 
    telefone = models.CharField(max_length=12)
    celular = models.CharField(max_length=13)
    data_modificacao = models.DateTimeField(default=datetime.now, blank=True)


class redesSociais(models.Model):
    nomeRS = models.CharField(max_length=30)
    link = models.CharField(max_length=100)

