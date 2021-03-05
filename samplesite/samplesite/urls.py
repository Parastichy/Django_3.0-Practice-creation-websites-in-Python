"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


def index(request):
    resp = HttpResponse('Здесь будет', content_type='text/plan; charset=utf-8')
    resp.write(' главная')
    resp.writelines((' страница', ' сайта'))
    resp['keywords'] = 'Python, Django'
    return resp


urlpatterns = [
    path('bboard/', include('bboard.urls')),

    # Список маршрутов уровня проекта, включающий список маршрутов уровня приложения
    # path('bboard/', include([
    #     path('add/', BbCreateView.as_view(), name='add'),
    #     path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    #     path('', index, name='index'),
    # ])),

    path('admin/', admin.site.urls),
    path('', index, ),
]
