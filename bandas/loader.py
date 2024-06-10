from bandas.models import Band, Album, Song
import json

Band.objects.all().delete()
Album.objects.all().delete()
Song.objects.all().delete()

with open('bandas/json/bands.json') as f:
    bandas = json.load(f)
    for banda in bandas:
        Band.objects.create(
            name=banda['name'],
            genre=banda['genre'],
            formed_in=banda['formed_in'],
            nationality=banda['nationality']
        )


with open('bandas/json/albums.json') as f:
    albums = json.load(f)
    band_objects = {band.name: band for band in Band.objects.all()}
    for album_data in albums:
        band_name = album_data['band']
        band = band_objects.get(band_name)
        album = Album.objects.create(
            title=album_data['title'],
            release_year=album_data['release_year'],
            band=band
        )
        for song in album_data['songs']:
            Song.objects.create(
                title = song['title'],
                duration = song['duration'],
                album = album
            )
