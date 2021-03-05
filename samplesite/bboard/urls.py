from django.urls import path

from .views import index, by_rubric, BbCreateView

# Пример передачи контроллеру функций значений mode:
# vals = {'mode': 'index'}
urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),

    # Именованный маршрут
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    # Передача значений
    # path('<int:rubric_id>/', by_rubric, vals),
    path('', index, name='index'),
]
