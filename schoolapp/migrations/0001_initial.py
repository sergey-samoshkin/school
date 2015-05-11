# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('discipline', models.CharField(verbose_name='Предмет', max_length=50, default='')),
                ('description', models.CharField(verbose_name='Описание', max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='Время добавления', default=django.utils.timezone.now)),
                ('file', models.FileField(verbose_name='Файл', upload_to='hw_files', blank=True, null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('short_name', models.CharField(verbose_name='Краткое название', max_length=100, unique=True, help_text='Например "№30"')),
                ('full_name', models.CharField(verbose_name='Полное официальное название', max_length=300, unique=True)),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_year', models.PositiveIntegerField(verbose_name='Год начала обучения', default=2015)),
                ('letter', models.CharField(verbose_name='Буква класса', max_length=3, default='A')),
                ('skip_4th_grade', models.BooleanField(verbose_name='Класс пропустит 4ый', default=True)),
                ('graduate_at', models.PositiveSmallIntegerField(verbose_name='Номер в год выпуска', default=11)),
                ('login_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(to='schoolapp.School')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.AddField(
            model_name='homework',
            name='schoolclass',
            field=models.ForeignKey(to='schoolapp.SchoolClass'),
        ),
    ]
