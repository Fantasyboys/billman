# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True)),
                ('country_abbreviation', models.CharField(blank=True, max_length=2, null=True, verbose_name='País(Sigla)')),
                ('state_abbreviation', models.CharField(blank=True, max_length=20, null=True, verbose_name='Estado(Sigla)')),
                ('city', models.CharField(blank=True, max_length=60, null=True, verbose_name='Cidade')),
                ('full_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Endereço completo com CEP')),
                ('responsibles', models.CharField(blank=True, max_length=300, null=True, verbose_name='Responsáveis')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, verbose_name='Telefone')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('unit_price', models.FloatField(blank=True, null=True, verbose_name='Valor unitário')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Quantidade')),
            ],
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='phones',
            field=models.ManyToManyField(to='services_crud.CustomerPhone'),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services_crud.Service'),
        ),
    ]