from django.shortcuts import render, redirect
from .models import Band, Album, Song
from .forms import BandForm, AlbumForm, SongForm
from django.contrib.auth.decorators import login_required

def user_belongs_to_group(user, group):
    return user.groups.filter(name=group).exists()

def index_view(request):
    context = {}
    return render(request, 'bandas/index.html', context)

def band_list_view(request):
    bands = Band.objects.all()
    canUserManipulate = request.user.groups.filter(name='Editores de bandas').exists()

    context = {'bands': bands,'canUserManipulate':canUserManipulate}

    return render(request, 'bandas/bands.html', context)

def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {'album': album}
    return render(request, 'bandas/album.html', context)

def song_list_view(request, album_id):
    album = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album)
    canUserManipulate = request.user.groups.filter(name='Editores de bandas').exists()

    context = {'album': album, 'songs': songs, 'canUserManipulate':canUserManipulate}
    return render(request, 'bandas/album_songs.html', context)

def song_view(request, song_id):
    song = Song.objects.get(id=song_id)
    canUserManipulate = request.user.groups.filter(name='Editores de bandas').exists()

    context = {'song': song,'canUserManipulate':canUserManipulate}

    return render(request, 'bandas/song.html', context)

def band_detail_view(request, band_id):
    band = Band.objects.get(pk=band_id)
    albums = Album.objects.filter(band=band)
    canUserManipulate = request.user.groups.filter(name='Editores de bandas').exists()

    context = {'band': band, 'albums': albums, 'canUserManipulate':canUserManipulate}

    return render(request, 'bandas/band_detail.html', context)

def table_view(request):
    return render(request, 'bandas/html5-css.html')

################################################################################
#
#                                   BANDA
#
################################################################################

@login_required
def create_band_view(request):
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            band = form.save(commit=False)
            band.save()
            return redirect('bandas:band_detail', band_id=band.id)
    else:
        form = BandForm()
    return render(request, 'bandas/create_band.html', {'form': form})

@login_required
def edit_band_view(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        form = BandForm(request.POST, request.FILES, instance=band)
        if form.is_valid():
            form.save()
            return redirect('bandas:band_detail', band_id=band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'bandas/edit_band.html', {'form': form, 'band': band})

@login_required
def delete_band_view(request, band_id):
    band = Band.objects.get(id=band_id)
    if request.method == 'POST':
        band.delete()
        return redirect('bandas:band_list')
    else:
        return render(request, 'bandas/delete_band.html', {'band': band})

################################################################################
#
#                                   ALBUM
#
################################################################################

@login_required
def create_album_view(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
            return redirect('bandas:album_detail', album_id = album.id)
    else:
        form = AlbumForm()
    return render(request, 'bandas/create_album.html', {'form': form})

@login_required
def edit_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance = album)
        if form.is_valid():
            form.save()
            return redirect('bandas:album_detail', album_id)
    else:
        form = AlbumForm(instance = album)
    return render(request, 'bandas/edit_album.html', {'form': form, 'album': album})

@login_required
def delete_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    band_id = album.band.id
    if request.method == 'POST':
        album.delete()
        return redirect('bandas:band_detail', band_id)
    else:
        return render(request, 'bandas/delete_album.html', {'album': album})


################################################################################
#
#                                   Song
#
################################################################################

@login_required
def create_song_view(request):
    if request.method == 'POST':
        form = SongForm(request.POST or None, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            return redirect('bandas:song_detail', song_id = song.id)
    else:
        form = SongForm()
    return render(request, 'bandas/create_song.html', {'form': form})

@login_required
def edit_song_view(request, song_id):
    song = Song.objects.get(id=song_id)
    if request.method == 'POST':
        form = SongForm(request.POST, instance = song)
        if form.is_valid():
            form.save()
            return redirect('bandas:song_detail', song_id)
    else:
        form = SongForm(instance = song)
    return render(request, 'bandas/edit_song.html', {'form': form, 'song': song})

@login_required
def delete_song_view(request, song_id):
    song = Song.objects.get(id=song_id)
    album_id = song.album.id
    if request.method == 'POST':
        song.delete()
        return redirect('bandas:album_detail', album_id)
    else:
        return render(request, 'bandas/delete_song.html', {'song': song})


























