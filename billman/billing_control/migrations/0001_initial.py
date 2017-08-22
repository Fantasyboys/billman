# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services_crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attach_bill', models.BooleanField(default=False, verbose_name='Gerar boleto')),
                ('active', models.BooleanField(default=False, verbose_name='Ativo')),
                ('send_montly_day', models.DateField(verbose_name='Data de envio')),
                ('duedate', models.DateField(verbose_name='Vencimento')),
                ('paid', models.BooleanField(default=False, verbose_name='Pago')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services_crud.CustomerDetails', verbose_name='Cliente')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services_crud.Service', verbose_name='Serviço')),
            ],
            options={
                'verbose_name_plural': 'Controles de Cobrança',
                'verbose_name': 'Controle de Cobrança',
            },
        ),
        migrations.CreateModel(
            name='BillingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('value', models.FloatField(blank=True, null=True, verbose_name='Valor')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Atualizado em')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services_crud.CustomerDetails', verbose_name='Cliente')),
            ],
            options={
                'verbose_name_plural': 'Históricos de Cobranças',
                'verbose_name': 'Histórico de Cobranças',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ScheduledPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateField(verbose_name='Data de envio')),
                ('duedate', models.DateField(verbose_name='Vencimento')),
                ('description', models.CharField(max_length=500, verbose_name='Descrição')),
                ('unit_price', models.FloatField(blank=True, null=True, verbose_name='Valor unitário')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Quantidade')),
                ('attach_bill', models.BooleanField(default=False, verbose_name='Gerar boleto')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services_crud.CustomerDetails', verbose_name='Cliente')),
            ],
            options={
                'verbose_name_plural': 'Agendamentos de Cobranças',
                'verbose_name': 'Agendamento de Cobrança',
            },
        ),
    ]