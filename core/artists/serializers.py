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
    
    artist = serializers.CharField(source='artist.name')  # This will return the artist's name

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'audio_file', 'duration', 'created_at', 'is_liked']

    is_liked = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user in obj.liked_by.all()
    
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_date']

class ArtistDetailSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True, source='album_set')
    songs = SongSerializer(many=True, read_only=True, source='songs')

    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'albums', 'songs']

