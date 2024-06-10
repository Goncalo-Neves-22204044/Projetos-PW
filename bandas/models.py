from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    formed_in = models.IntegerField()
    nationality = models.CharField(max_length=100, default='N/A')
    numArtists = models.IntegerField(default=1)
    photo = models.ImageField(null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name = 'albums')
    photo = models.ImageField(upload_to="imgs", null=True, blank=True, default=None)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.CharField(max_length=100, default="Erro")
    spotify_link = models.URLField(blank=True, null=True)
    letra = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.title
