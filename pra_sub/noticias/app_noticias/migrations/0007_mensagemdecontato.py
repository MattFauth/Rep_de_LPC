# Generated by Django 2.2.5 on 2019-12-10 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0006_auto_20191210_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensagemDeContato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Mensagem de contato',
                'verbose_name_plural': 'Mensagens de contato',
            },
        ),
    ]
