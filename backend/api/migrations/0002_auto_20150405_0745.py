# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='angry',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mood',
            name='happy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mood',
            name='sad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mood',
            name='surprised',
            field=models.FloatField(),
        ),
    ]
