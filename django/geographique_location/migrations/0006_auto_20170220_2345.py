# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 23:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geographique_location', '0005_auto_20170220_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='dateUpdate',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 20, 23, 45, 43, 677550)),
        ),
    ]
