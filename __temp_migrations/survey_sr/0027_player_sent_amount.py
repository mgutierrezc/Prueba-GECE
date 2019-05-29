# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-08 16:01
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_sr', '0026_auto_20190329_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='sent_amount',
            field=otree.db.models.IntegerField(default=0, null=True, verbose_name='Deslice hasta escoger la cantidad a enviar deseada'),
        ),
    ]