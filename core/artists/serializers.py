from rest_framework import serializers
from .models import Artist, Song, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'followers_count']

    followers_count = serializers.SerializerMethodField()

    def get_followers_count(self, obj):
        return obj.followers.count()
    
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'audio_file', 'duration', 'created_at']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_date']
