# Generated by Django 2.2.5 on 2019-12-10 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0004_autor_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_noticias.Pessoa'),
        ),
    ]