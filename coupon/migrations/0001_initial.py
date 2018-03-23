# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-22 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=7)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
