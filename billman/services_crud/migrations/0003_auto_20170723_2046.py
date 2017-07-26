# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_crud', '0002_auto_20170723_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerdetails',
            options={'verbose_name': 'Detalhe do cliente', 'verbose_name_plural': 'Detalhes do cliente'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Serviço', 'verbose_name_plural': 'Serviços'},
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='phones',
            field=models.ManyToManyField(blank=True, to='services_crud.CustomerPhone'),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='services',
            field=models.ManyToManyField(blank=True, to='services_crud.Service'),
        ),
    ]
