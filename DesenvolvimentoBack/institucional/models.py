from django.db import models
from datetime import datetime

class quemSomos(models.Model):
    apresentacao = models.TextField()
    #imagem
    titulo = models.CharField(max_length=50)
    data_modificacao = models.DateTimeField(default=datetime.now, blank=True)

class contato(models.Model):
    email = models.CharField(max_length=255) 
    telefone = models.CharField(max_length=12)
    celular = models.CharField(max_length=13)
    data_modificacao = models.DateTimeField(default=datetime.now, blank=True)

class redesSociais(models.Model):
    nomeRS = models.CharField(max_length=30)
    link = models.CharField(max_length=100)

class servicos(models.Model):
    nome = models.CharField(max_length=50)
    descrição_do_servico = models.TextField()
    preço = models.CharField(max_length=13)