from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
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


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
