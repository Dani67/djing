# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-06 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0011_auto_20170116_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='media/task_attachments/%Y.%m.%d'),
        ),
    ]