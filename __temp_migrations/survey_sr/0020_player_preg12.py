# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-29 22:36
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_sr', '0019_auto_20190329_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='preg12',
            field=otree.db.models.StringField(choices=[('Si', 'Si'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Usted notificaría el error?'),
        ),
    ]