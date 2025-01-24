from django.db import models
from django.conf import settings

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following_artists', blank=True)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/')
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_songs', blank=True)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
