from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('cursos/', views.cursos_view, name='cursos'),
    path('cursos/<int:curso_id>', views.curso_details_view, name='curso_details'),
    path('disciplina/<int:disciplina_id>', views.disciplina, name='disciplina'),
    path('projeto/<int:projeto_id>', views.projeto_view, name='projeto'),
    path('linguagem/<int:linguagem_id>', views.linguagem_view, name='linguagem'),

    path('cursos/create', views.create_curso, name='create_curso'),
    path('cursos/edit/<int:curso_id>', views.edit_curso, name='edit_curso'),
    path('cursos/delete/<int:curso_id>', views.delete_curso, name='delete_curso'),

    path('disciplina/create', views.create_disciplina, name='create_disciplina'),
    path('disciplina/edit/<int:disciplina_id>', views.edit_disciplina, name='edit_disciplina'),
    path('disciplina/delete/<int:disciplina_id>', views.delete_disciplina, name='delete_disciplina'),


    path('projeto/create', views.create_projeto, name='create_projeto'),
    path('projeto/edit/<int:projeto_id>', views.edit_projeto, name='edit_projeto'),
    path('projeto/delete/<int:projeto_id>', views.delete_projeto, name='delete_projeto'),

    path('linguagem/create', views.create_linguagem, name='create_linguagem'),
    path('linguagem/edit/<int:linguagem_id>', views.edit_linguagem, name='edit_linguagem'),
    path('linguagem/delete/<int:linguagem_id>', views.delete_linguagem, name='delete_linguagem'),


]
