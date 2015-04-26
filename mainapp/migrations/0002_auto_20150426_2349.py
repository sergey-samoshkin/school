# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolclass',
            name='graduate_at',
            field=models.PositiveSmallIntegerField(default=11, verbose_name='Номер в год выпуска'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='skip_4th_grade',
            field=models.BooleanField(default=True, verbose_name='Класс пропустит 4ый'),
        ),
    ]
