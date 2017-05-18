# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-10 23:17
from __future__ import unicode_literals

from django.db import migrations
import mydefs


class Migration(migrations.Migration):

    dependencies = [
        ('abonapp', '0018_auto_20170418_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='abon',
            name='ip_address',
            field=mydefs.MyGenericIPAddressField(blank=True, max_length=8, null=True, protocol='ipv4'),
        ),
    ]