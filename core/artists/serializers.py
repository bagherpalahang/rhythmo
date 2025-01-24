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
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'audio_file', 'duration', 'created_at', 'is_liked']

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user in obj.liked_by.all()

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'release_date']
