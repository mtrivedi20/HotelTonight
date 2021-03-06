# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casedata', '0003_auto_20170212_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='neighborhood',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='point',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='casedata.Point'),
        ),
        migrations.AlterField(
            model_name='case',
            name='request_details',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='request_type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='responsible_agency',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='source',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='status_notes',
            field=models.CharField(default='', max_length=200),
        ),
    ]
