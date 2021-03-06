# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_title', models.CharField(max_length=200)),
                ('stocktag_str', models.CharField(max_length=200)),
                ('stocktag_num', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stocklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='stocklist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocklist.Stocklist'),
        ),
    ]
