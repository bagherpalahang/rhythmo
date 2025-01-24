from django.contrib import admin
from .models import Artist, Album, Song

# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio') 
    search_fields = ('name',)
    ordering = ('name',) 

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    search_fields = ('title', 'artist__name')
    list_filter = ('artist', 'release_date')
    ordering = ('title',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'duration')
    search_fields = ('title', 'artist__name', 'album__title')
    list_filter = ('artist', 'album')
    ordering = ('title',)