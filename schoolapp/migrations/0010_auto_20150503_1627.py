# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def add_permission(apps,schema_editor):
    Group = apps.get_model("auth","Group")
    Permission = apps.get_model("auth","Permission")
    teacher_group = Group.objects.filter(name="Учитель")[0]
    teacher_group.permissions.add(
        Permission.objects.get(codename='delete_homework',content_type__app_label='schoolapp'),
    )

class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_auto_20150503_1435'),
    ]

    operations = [
        migrations.RunPython(add_permission,reverse_code=lambda *args,**kwargs: True)
    ]
