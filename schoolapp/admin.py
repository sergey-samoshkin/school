from django.contrib import admin
from .models import School, SchoolClass


admin.AdminSite.site_header = 'Администрирование школ'


class ClassInline(admin.TabularInline):
    model = SchoolClass
    verbose_name = 'Класс'
    verbose_name_plural = 'Классы'
    fields = ['start_year', 'letter', 'login_user']
    extra = 3


class SchoolAdmin(admin.ModelAdmin):
    inlines = [ClassInline]
    list_display = ('short_name', 'full_name')
    search_fields = ['full_name']


class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['school', 'start_year', 'letter']}),
        ('Доступ',           {'fields': ['login_user']}),
        ('Дополнительно',    {'fields': ['skip_4th_grade', 'graduate_at'], 'classes': ['collapse']}),
    ]
    list_display = ('__str__', 'start_year', 'number', 'letter',)
    list_filter = ['start_year', 'letter',]


admin.site.register(School, SchoolAdmin)
admin.site.register(SchoolClass, ClassAdmin)
