# Generated by Django 2.2.5 on 2019-10-19 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_processo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='resumo',
            field=models.TextField(blank=True, null=True, verbose_name='Resumo do processo'),
        ),
    ]