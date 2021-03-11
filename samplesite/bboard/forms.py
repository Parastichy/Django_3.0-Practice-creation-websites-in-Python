from django.core import validators

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DecimalField, modelform_factory
from django.forms.widgets import Select
from django import forms
from .models import Bb, Rubric


# Использование быстрого объявления формы связанной с моделью
# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'kind', 'rubric')
#         labels = {'title': 'Название товара'}
#         help_texts = {'rubric': 'Не забудьте задать рубрику!'}
#         field_classes = {'pruce': DecimalField}
#         widgets = {'rubric': Select(attrs={'size': 8})}


# Использование фабрики класов для создания формы
# Создаёться только по необходимости
# И уничтажаеться сразу после того как перестанет
# хрянязая его переменная (экономит оперативную память) !!! только для редко используемых форм
# BbForm = modelform_factory(Bb,
#                            fields=('title', 'content', 'price', 'rubric'),
#                            labels={'title': 'Название товара'},
#                            help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
#                            field_classes={'price': DecimalField},
#                            widgets={'rubric': Select(attrs={'size': 8})}
#                            )

# Создание формы путём полного объявления
# Сложный вариант который позволяет описать поля формы во всех деталях
class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара', validators=[validators.MinLengthValidator(4)],
                            error_messages={'min_length': 'Слишком короткое название товара'})
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), label='Рубрика',
                                    help_text='Не забудьте выбрать рубрику!',
                                    widget=forms.widgets.Select(attrs={'size': 8}))

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')

    def clean_title(self):
        val = self.cleaned_data['title']
        if val == 'Прошлогодний снег':
            raise ValidationError('К продаже не допускается')
        return val


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Пароль (повторно)')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')
