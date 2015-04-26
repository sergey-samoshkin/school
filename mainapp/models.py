from django.db import models
from datetime import date


# Начало учебного года в сентябре
START_MONTH = 9


class School(models.Model):
    short_name = models.CharField('Краткое название', max_length=100)
    full_name = models.CharField('Полное официальное название', max_length=300)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return self.short_name


class SchoolClass(models.Model):
    school = models.ForeignKey(School)
    start_year = models.PositiveIntegerField('Год начала обучения', default=date.today().year)
    letter = models.CharField('Буква класса', default='A', max_length=3)
    skip_4th_grade = models.BooleanField('Класс пропустит 4ый', default=True)
    graduate_at = models.PositiveSmallIntegerField('Номер в год выпуска', default=11)

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def number(self):
        today = date.today()
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
