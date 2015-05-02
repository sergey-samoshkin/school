# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0005_homework_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(null=True, blank=True, upload_to='', verbose_name='Файл'),
        ),
    ]
