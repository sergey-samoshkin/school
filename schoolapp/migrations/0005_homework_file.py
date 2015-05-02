# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_auto_20150502_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='file',
            field=models.FileField(upload_to='', verbose_name='Файл', default=None),
        ),
    ]
