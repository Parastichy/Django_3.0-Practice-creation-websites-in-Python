from django.urls import path

from .views import index, by_rubric, BbCreateView, add_and_save, BbDetailView

# Пример передачи контроллеру функций значений mode:
# vals = {'mode': 'index'}
urlpatterns = [
    path('add/', add_and_save, name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),

    # path('add/', BbCreateView.as_view(), name='add'),

    # Именованный маршрут
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    # Передача значений
    # path('<int:rubric_id>/', by_rubric, vals),
    path('', index, name='index'),
]
