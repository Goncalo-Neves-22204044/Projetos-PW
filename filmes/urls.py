from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('filmes/', views.movie_list, name='movie_list'),
    path('filmes/<int:movie_id>/', views.movie_detail, name='movie_detail')
]
