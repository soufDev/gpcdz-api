# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographique_location', '0004_auto_20170220_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='dateUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
