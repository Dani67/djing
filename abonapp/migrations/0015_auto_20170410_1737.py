# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-10 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abonapp', '0014_auto_20170330_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abon',
            name='opt82',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='abonapp.Opt82'),
        ),
    ]
