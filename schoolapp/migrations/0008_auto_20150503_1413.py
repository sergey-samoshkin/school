# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def make_permissions(apps,schema_editor):
    Group = apps.get_model("auth","Group")
    Permission = apps.get_model("auth","Permission")
    teacher_group = Group.objects.filter(name="Учитель")
    if len(teacher_group) == 0:
        teacher_group = Group(name="Учитель")
        teacher_group.save()
    else:
        teacher_group = teacher_group[0]
    teacher_group.permissions.add(
        Permission.objects.get(codename='add_homework',content_type__app_label='schoolapp'),
        Permission.objects.get(codename='add_schoolclass',content_type__app_label='schoolapp'),
        Permission.objects.get(codename='change_schoolclass',content_type__app_label='schoolapp'),
        Permission.objects.get(codename='delete_schoolclass',content_type__app_label='schoolapp'),
    )

class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0007_auto_20150502_2258'),
    ]

    operations = [
        migrations.RunPython(make_permissions,reverse_code=lambda *args,**kwargs: True)
    ]
