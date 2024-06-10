from django.shortcuts import render
from .models import Movie, Actor, Genre
from datetime import datetime

def movie_list(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    current_year = datetime.now().year
    context = {'movies': movies, 'genres': genres, 'current_year': current_year}
    return render(request, 'filmes/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    current_year = datetime.now().year
    print(current_year)
    context = {'movie': movie, 'current_year': current_year}
    return render(request, 'filmes/movie_detail.html', context)