# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20170323_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='comment',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]