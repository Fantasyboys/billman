# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_crud', '0006_auto_20170726_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='phones',
            field=models.ManyToManyField(blank=True, to='services_crud.CustomerPhone', verbose_name='Telefones'),
        ),
    ]
