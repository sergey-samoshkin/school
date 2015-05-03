# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schoolapp', '0006_auto_20150502_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='created_by',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homework',
            name='discipline',
            field=models.CharField(default='', max_length=50, verbose_name='Предмет'),
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='login_user',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='homework',
            name='file',
            field=models.FileField(blank=True, null=True, verbose_name='Файл', upload_to='hw_files'),
        ),
    ]
