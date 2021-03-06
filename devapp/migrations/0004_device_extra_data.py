# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 10:59
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('devapp', '0003_auto_20180529_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='extra_data',
            field=jsonfield.fields.JSONField(blank=True, help_text='Extra data in JSON format. You may use it for your custom data', null=True, verbose_name='Extra data'),
        ),
    ]
