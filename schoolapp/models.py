from django.db import models
from django.utils import timezone


# Начало учебного года в сентябре
START_MONTH = 9


class School(models.Model):
    short_name = models.CharField('Краткое название', max_length=100, unique=True, help_text='Например "№30"')
    full_name = models.CharField('Полное официальное название', max_length=300, unique=True)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return self.short_name


class SchoolClass(models.Model):
    school = models.ForeignKey(School)
    start_year = models.PositiveIntegerField('Год начала обучения', default=timezone.now().year)
    letter = models.CharField('Буква класса', default='A', max_length=3)
    skip_4th_grade = models.BooleanField('Класс пропустит 4ый', default=True)
    graduate_at = models.PositiveSmallIntegerField('Номер в год выпуска', default=11)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def number(self):
        today = timezone.now().date()
        result = today.year - self.start_year
        if today.month >= START_MONTH:
            result += 1
        if self.skip_4th_grade and result >= 4:
            result += 1
        if result > self.graduate_at:
            return self.graduate_at
        return result

    number.admin_order_field = 'start_year'
    number.short_description = 'Класс'

    def __str__(self):
        return "%s%s" % (self.number(), self.letter)

    def add_home_work(self, description, file=None):
        hw = HomeWork(schoolclass=self, description=description, file=file)
        hw.save()


class HomeWork(models.Model):
    schoolclass = models.ForeignKey(SchoolClass)
    description = models.CharField('Описание', max_length=200)
    created_at = models.DateTimeField('Время добавления', default=timezone.now)
    file = models.FileField('Файл', null=True, blank=True, upload_to='hw_files')

