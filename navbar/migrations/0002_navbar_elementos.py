# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-23 00:36
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbar',
            name='elementos',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
