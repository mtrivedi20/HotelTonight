# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casedata', '0005_auto_20170212_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='status_notes',
            field=models.CharField(default='', max_length=300),
        ),
    ]
