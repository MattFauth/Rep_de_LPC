# Generated by Django 2.2.5 on 2019-12-06 23:25

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
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, max_length=120, null=True, verbose_name='Nome do cargo')),
                ('ehchefe', models.BooleanField(blank=True, null=True, verbose_name='Eh chefe?')),
                ('ehmotorista', models.BooleanField(blank=True, null=True, verbose_name='Eh motorista?')),
                ('ehtransp', models.BooleanField(blank=True, null=True, verbose_name='Eh Chefe do transporte?')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, max_length=120, null=True, verbose_name='Nome do departamento')),
                ('codigo', models.TextField(blank=True, max_length=4, null=True, verbose_name='Codigo do departamento')),
                ('ehTransp', models.BooleanField(blank=True, null=True, verbose_name='Eh transporte?')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(blank=True, max_length=120, null=True, verbose_name='Nome do funcionario')),
                ('matricula', models.TextField(blank=True, max_length=6, null=True, verbose_name='Matricula do funcionario')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_empresa.Cargo')),
                ('dep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_empresa.Departamento')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.TextField(blank=True, help_text='No formato AAA-0000', max_length=8, null=True, verbose_name='Placa do carro')),
                ('descricao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descricao do veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origem', models.TextField(blank=True, max_length=120, null=True, verbose_name='Origem da viagem')),
                ('destino', models.TextField(blank=True, max_length=120, null=True, verbose_name='Destino da viagem')),
                ('data', models.DateTimeField(blank=True, null=True, verbose_name='Data e hora da viagem')),
                ('qtppl', models.TextField(max_length=1, verbose_name='Quantidade de passageiros')),
                ('func', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_empresa.Funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_empresa.Funcionario')),
                ('solicitacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_empresa.Solicitacao')),
                ('veiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_empresa.Veiculo')),
            ],
        ),
    ]
