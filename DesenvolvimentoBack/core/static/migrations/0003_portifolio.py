# Generated by Django 3.2 on 2021-04-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucional', '0002_auto_20210407_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_port', models.TextField()),
            ],
        ),
    ]
