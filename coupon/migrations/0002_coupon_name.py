# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
