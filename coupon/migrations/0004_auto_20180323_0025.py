# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0003_auto_20180322_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
