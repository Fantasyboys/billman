# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing_control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingcontrol',
            name='duedate',
        ),
        migrations.RemoveField(
            model_name='billingcontrol',
            name='send_montly_day',
        ),
    ]
