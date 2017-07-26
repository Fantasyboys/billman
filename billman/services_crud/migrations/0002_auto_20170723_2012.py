# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerdetails',
            options={'verbose_name': 'Detalhe do usuário', 'verbose_name_plural': 'Detalhes do usuário'},
        ),
        migrations.AlterModelOptions(
            name='customerphone',
            options={'verbose_name': 'Telefone', 'verbose_name_plural': 'Telefones'},
        ),
        migrations.RemoveField(
            model_name='customerdetails',
            name='services',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='services',
            field=models.ManyToManyField(to='services_crud.Service'),
        ),
    ]