# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20171017_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='freshman_year',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='special_diet',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='table_company',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
