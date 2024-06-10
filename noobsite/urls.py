# noobsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('index/', views.index_view, name = 'index'),
    path('helloWorld/', views.helloWorld),
    path('name/', views.getName),
    path('age/', views.getAge),

]