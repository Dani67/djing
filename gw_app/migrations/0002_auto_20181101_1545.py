# Generated by Django 2.1 on 2018-11-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nasmodel',
            options={'ordering': ('ip_address',), 'verbose_name': 'Network access server. Gateway', 'verbose_name_plural': 'Network access servers. Gateways'},
        ),
        migrations.AlterField(
            model_name='nasmodel',
            name='auth_login',
            field=models.CharField(max_length=64, verbose_name='Auth login'),
        ),
        migrations.AlterField(
            model_name='nasmodel',
            name='auth_passw',
            field=models.CharField(max_length=127, verbose_name='Auth password'),
        ),
    ]
