# Generated by Django 2.2.20 on 2021-04-11 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0015_delete_redessociais'),
    ]

    operations = [
        migrations.AddField(
            model_name='painel',
            name='data_modificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Data de modificação'),
        ),
        migrations.AddField(
            model_name='portifolio',
            name='data_modificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Data de modificação'),
        ),
        migrations.AddField(
            model_name='servicos',
            name='data_modificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Data de modificação'),
        ),
    ]
