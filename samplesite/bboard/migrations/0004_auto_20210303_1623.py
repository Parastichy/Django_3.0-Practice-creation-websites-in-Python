# Generated by Django 3.1.7 on 2021-03-03 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bboard', '0003_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[(None, 'Выбирите тип публикуемого объявления'), ('Купля-продажа', (('b', 'Куплю'), ('s', 'Продам'))), ('Обмен', (('c', 'Обменяю'),))], default='s', max_length=1, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activated', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]