from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView

from .views import index, by_rubric, add_and_save, BbDetailView, BbEditView, BbDeleteView, BbIndexView, \
    BbDayArchiveView, rubrics_edit

# Пример передачи контроллеру функций значений mode:
# vals = {'mode': 'index'}
urlpatterns = [
    path('add/', add_and_save, name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', BbEditView.as_view(), name='edit'),
    path('edit_rubric/', rubrics_edit, name='edit_rubric'),
    path('delete/<int:pk>/', BbDeleteView.as_view(), name='delete'),
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),

    # path('add/', BbCreateView.as_view(), name='add'),

    # Именованный маршрут
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),

    # Передача значений
    # path('<int:rubric_id>/', by_rubric, vals),
    path('', index, name='index'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/bboard/'), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(template_name='registration/change_password.html'),
         name='password_change_done'),
    path('accounts/password_reset/', PasswordResetView.as_view(template_name='registration/reset_password.html',
                                                               subject_template_name='registration/reset_subject.txt',
                                                               email_template_name='registration/reset_email.txt'),
         name='password_reset'),
    # path('', BbIndexView.as_view(), name='index'),
    path('<int:year>/<int:month>/<int:day>/', BbDayArchiveView.as_view()),
]
