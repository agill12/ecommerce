# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_coupon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.FloatField(),
        ),
    ]
