# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-08 17:16
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_sr', '0030_auto_20190408_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='preg31',
            field=otree.db.models.IntegerField(default=0, null=True, verbose_name='¿Cuánto pondría en la cuenta pública?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='preg32',
            field=otree.db.models.IntegerField(default=0, null=True, verbose_name='Si fueran 100 soles en vez de 10. ¿Cuánto pondría en la cuenta pública?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='preg33',
            field=otree.db.models.IntegerField(default=0, null=True, verbose_name='Si fueran 1000 soles en vez de 10. ¿Cuánto pondría en la cuenta pública?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='preg34',
            field=otree.db.models.IntegerField(default=0, null=True, verbose_name='Si fueran 100000 soles en vez de 10. ¿Cuánto pondría en la cuenta pública?'),
        ),
    ]