# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0008_auto_20150503_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='login_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
