from django.forms import ModelForm, DecimalField, modelform_factory
from django.forms.widgets import Select
from .models import Bb

# Использование быстрого объявления формы связанной с моделью
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'kind', 'rubric')
        labels = {'title': 'Название товара'}
        help_texts = {'rubric': 'Не забудьте задать рубрику!'}
        field_classes = {'pruce': DecimalField}
        widgets = {'rubric': Select(attrs={'size': 8})}


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
