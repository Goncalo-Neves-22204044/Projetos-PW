from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('article/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),

    path('article/create/', views.create_article, name='create_article'),
    path('article/edit/<int:article_id>', views.edit_article, name='edit_article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),

    path('author/create/', views.create_author, name='create_author'),
    path('author/edit/<int:author_id>/', views.edit_author, name='edit_author'),
    path('author/delete/<int:author_id>/', views.delete_author, name='delete_author')
]
