# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180304_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]
