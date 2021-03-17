from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError(f'Число {val} нечетное', code='odd')


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена', validators=[validate_even])
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    KINDS = ((None, 'Выбирите тип публикуемого объявления'),
             ('Купля-продажа', (('b', 'Куплю'), ('s', 'Продам'))),
             ('Обмен', (('c', 'Обменяю'),)))
    kind = models.CharField(max_length=1, choices=KINDS, default='s', verbose_name='Тип')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объвление'
        ordering = ['-published']
        # index_together = [
        #     ['published', 'title'],
        #     ['title', 'price', 'rubric'],
        #     ]

    def title_and_price(self):  # Функциональное поле
        if self.price:
            return '%s (%.2f)' % (self.title, self.price)
        else:
            return self.price

    # Название функционального поля необязательный атрибут.
    title_and_price.short_description = 'Название и цена'

    def clean(self):
        errors = {}
        if not self.content:
            errors['content'] = ValidationError('Укажите описание продоваемого товара')

        if self.price and self.price < 0:
            errors['price'] = ValidationError('Укажите не отрицательное значение цены')

        if errors:
            raise ValidationError(errors)


class RubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('order', 'name')

    def order_by_bb_count(self):
        return super().get_queryset().annotate(cnt=models.Count('bb')).order_by('-cnt')


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    objects = models.Manager()
    bbs = RubricManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/bboard/{self.pk}/'

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
