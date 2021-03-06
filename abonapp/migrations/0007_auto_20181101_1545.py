# Generated by Django 2.1 on 2018-11-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw_app', '0002_auto_20181101_1545'),
        ('abonapp', '0006_change_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abon',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='Ip address'),
        ),
        migrations.AlterUniqueTogether(
            name='abon',
            unique_together={('ip_address', 'nas')},
        ),
    ]
