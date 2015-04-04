# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('angry', models.DecimalField(max_digits=7, decimal_places=6)),
                ('sad', models.DecimalField(max_digits=7, decimal_places=6)),
                ('surprised', models.DecimalField(max_digits=7, decimal_places=6)),
                ('happy', models.DecimalField(max_digits=7, decimal_places=6)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
