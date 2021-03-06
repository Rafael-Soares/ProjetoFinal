# Generated by Django 3.1.7 on 2021-04-07 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=12)),
                ('celular', models.CharField(max_length=13)),
                ('data_modificacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='quemSomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apresentacao', models.TextField()),
                ('titulo', models.CharField(max_length=30)),
                ('data_modificacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='redesSociais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeRS', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='servicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descrição_do_servico', models.TextField()),
                ('preço', models.CharField(max_length=13)),
            ],
        ),
    ]
