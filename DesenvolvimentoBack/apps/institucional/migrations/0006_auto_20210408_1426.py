# Generated by Django 3.1.7 on 2021-04-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0005_quemsomos_imageqs'),
    ]

    operations = [
        migrations.CreateModel(
            name='painel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sloganPainel', models.CharField(max_length=255)),
                ('imagePainel', models.ImageField(blank=True, upload_to='imagens/')),
            ],
        ),
        migrations.RenameField(
            model_name='portifolio',
            old_name='descricao_port',
            new_name='descricaoPortifolio',
        ),
        migrations.RenameField(
            model_name='quemsomos',
            old_name='imageQS',
            new_name='imageQuemSomos',
        ),
        migrations.AddField(
            model_name='portifolio',
            name='imagePortifolio',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
        migrations.AddField(
            model_name='servicos',
            name='imageServico',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
    ]