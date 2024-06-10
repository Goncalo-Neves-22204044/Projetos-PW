from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.name}'

class Genre(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name = 'genre')
    release_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return f'{self.title}'
