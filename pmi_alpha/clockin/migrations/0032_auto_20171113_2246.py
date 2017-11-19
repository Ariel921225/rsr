# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 03:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0031_auto_20171014_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='intern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clockin.Intern'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_in',
            field=models.TimeField(blank=True, default=datetime.time(22, 46, 56, 842061), verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_out',
            field=models.TimeField(blank=True, default=datetime.time(22, 46, 56, 842089), verbose_name='Time Out'),
        ),
    ]
