# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0002_auto_20150426_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(verbose_name='Описание', max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 5, 1, 22, 44, 33, 785111, tzinfo=utc), verbose_name='Время добавления')),
            ],
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name': 'Школа', 'verbose_name_plural': 'Школы'},
        ),
        migrations.AlterModelOptions(
            name='schoolclass',
            options={'verbose_name': 'Класс', 'verbose_name_plural': 'Классы'},
        ),
        migrations.AlterField(
            model_name='school',
            name='full_name',
            field=models.CharField(verbose_name='Полное официальное название', max_length=300, unique=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='short_name',
            field=models.CharField(verbose_name='Краткое название', max_length=100, help_text='Например "№30"', unique=True),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='letter',
            field=models.CharField(default='A', max_length=3, verbose_name='Буква класса'),
        ),
        migrations.AlterField(
            model_name='schoolclass',
            name='start_year',
            field=models.PositiveIntegerField(default=2015, verbose_name='Год начала обучения'),
        ),
        migrations.AddField(
            model_name='homework',
            name='schoolclass',
            field=models.ForeignKey(to='schoolapp.SchoolClass'),
        ),
    ]
