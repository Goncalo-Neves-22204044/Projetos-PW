from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('bands/', views.band_list_view, name='band_list'),
    path('bands/<int:band_id>/', views.band_detail_view, name='band_detail'),
    path('album/<int:album_id>/', views.song_list_view, name='album_detail'),
    path('song/<int:song_id>/', views.song_view, name='song_detail'),

    path('bands/create/', views.create_band_view, name='create_band'),
    path('bands/edit/<int:band_id>/', views.edit_band_view, name='edit_band'),
    path('bands/delete/<int:band_id>/', views.delete_band_view, name='delete_band'),

    path('album/create/', views.create_album_view, name='create_album'),
    path('album/edit/<int:album_id>/', views.edit_album_view, name='edit_album'),
    path('album/delete/<int:album_id>/', views.delete_album_view, name='delete_album'),

    path('song/create/', views.create_song_view, name='create_song'),
    path('song/edit/<int:song_id>/', views.edit_song_view, name='edit_song'),
    path('song/delete/<int:song_id>/', views.delete_song_view, name='delete_song'),

    path('table/', views.table_view, name='table'),
]
