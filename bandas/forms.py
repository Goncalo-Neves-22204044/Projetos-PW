from django import forms
from .models import Band, Album, Song

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'formed_in', 'nationality', 'numArtists', 'photo', 'biografia']
        help_texts = {
            'name': 'Enter the name of the band.',
            'genre': 'Enter the genre of the band.',
            'formed_in': 'Enter the year the band was formed.',
            'nationality': 'Enter the nationality of the band.',
            'numArtists': 'Enter the number of artists in the band.',
            'photo': 'Upload a photo of the band.',
            'biografia' : 'Enter the biography for the band.'
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_year',  'band', 'photo']
        help_texts = {
            'title': 'Enter the title of the album.',
            'release_year': 'Enter the year the album was released.',
            'band': 'Select the band that released the album.',
            'photo': 'Upload a photo of the album cover.'
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album',  'duration', 'spotify_link', 'letra']
        help_texts = {
            'title': 'Enter the title of the song.',
            'album': 'Select the album the song belongs to.',
            'duration': 'Enter the duration of the song in seconds.',
            'spotify_link': 'Enter the Spotify link for the song.',
            'letra': 'Enter the lyrics for the song.'
        }
