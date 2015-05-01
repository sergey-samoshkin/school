# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('short_name', models.CharField(verbose_name='Краткое название', max_length=100)),
                ('full_name', models.CharField(verbose_name='Полное официальное название', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_year', models.PositiveIntegerField(default=2015, verbose_name='Год')),
                ('letter', models.CharField(default='A', verbose_name='Буква', max_length=3)),
                ('school', models.ForeignKey(to='schoolapp.School')),
            ],
        ),
    ]
