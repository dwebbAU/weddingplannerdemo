# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='budget',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
