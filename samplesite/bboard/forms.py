from django.forms import ModelForm, DecimalField, modelform_factory
from django.forms.widgets import Select
from .models import Bb

# class BbForm(ModelForm):
#     class Meta:
#         model = Bb
#         fields = ('title', 'content', 'price', 'kind', 'rubric')

# Использование фабрики класов
BbForm = modelform_factory(Bb,
                           fields=('title', 'content', 'price', 'rubric'),
                           labels={'title': 'Название товара'},
                           help_texts={'rubric': 'Не забудьте выбрать рубрику!'},
                           field_classes={'price': DecimalField},
                           widgets={'rubric': Select(attrs={'size': 8})}
                           )
