# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geographique_location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geolocation',
            old_name='userName',
            new_name='userName_createdBy',
        ),
    ]
