# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20161101_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.CharField(default='fa fa-bell-o', max_length=100),
            preserve_default=False,
        ),
    ]