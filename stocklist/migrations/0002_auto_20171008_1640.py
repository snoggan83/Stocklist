# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='in_portfolio',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='stocktag_num',
            field=models.IntegerField(),
        ),
    ]
