# Generated by Django 3.1.7 on 2021-04-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0011_auto_20210409_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painel',
            name='imagePainel',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
    ]
