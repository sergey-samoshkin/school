# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_auto_20150502_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время добавления'),
        ),
    ]
