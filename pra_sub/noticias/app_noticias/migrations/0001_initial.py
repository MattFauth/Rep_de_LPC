# Generated by Django 2.2.5 on 2019-12-11 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=120, verbose_name='Nome do departamento')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
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
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, max_length=120, null=True, verbose_name='Nome do autor')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('tel_cel', models.CharField(blank=True, help_text='Numero no formato (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone Celular')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Endereco de email')),
                ('autor', models.BooleanField()),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, max_length=120, null=True, verbose_name='Titulo da noticia')),
                ('conteudo', models.TextField(blank=True, null=True, verbose_name='Conteudo da noticia')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_noticias.Pessoa')),
                ('tags', models.ManyToManyField(to='app_noticias.Tag')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
    ]
