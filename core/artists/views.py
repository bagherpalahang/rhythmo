from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .serializers import ArtistSerializer, SongSerializer, AlbumSerializer
from .models import Artist, Song, Album

# Create your views here.

class FollowArtistView(APIView):
    def post(self, request, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        user = request.user

        if user in artist.followers.all():
            return Response({"message": "You are already following this artist."}, status=status.HTTP_400_BAD_REQUEST)

        artist.followers.add(user)
        return Response({"message": "You are now following this artist."}, status=status.HTTP_200_OK)

class UnfollowArtistView(APIView):
    def post(self, request, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        user = request.user

        if user not in artist.followers.all():
            return Response({"message": "You are not following this artist."}, status=status.HTTP_400_BAD_REQUEST)

        artist.followers.remove(user)
        return Response({"message": "You have unfollowed this artist."}, status=status.HTTP_200_OK)
    
class FollowedArtistsView(generics.ListAPIView):
    serializer_class = ArtistSerializer

    def get_queryset(self):
        return self.request.user.following_artists.all()

class FollowedArtistsContent(APIView):
    def get(self, request):
        user = request.user
        followed_artists = user.following_artists.all()

        songs = Song.objects.filter(artist__in=followed_artists).order_by('-created_at')
        albums = Album.objects.filter(artist__in=followed_artists).order_by('-release_date')

        song_serializer = SongSerializer(songs, many=True)
        album_serializer = AlbumSerializer(albums, many=True)

        combined_results = sorted(
            song_serializer.data + album_serializer.data,
            key=lambda x: x.get('created_at', x.get('release_date')),
            reverse=True
        )

        return Response(combined_results)

class LikeSongView(APIView):
    def post(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        user = request.user

        if user in song.liked_by.all():
            return Response({"message": "You have already liked this song."}, status=status.HTTP_400_BAD_REQUEST)

        song.liked_by.add(user)
        return Response({"message": "You have liked this song."}, status=status.HTTP_200_OK)

class UnlikeSongView(APIView):
    def post(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        user = request.user

        if user not in song.liked_by.all():
            return Response({"message": "You have not liked this song."}, status=status.HTTP_400_BAD_REQUEST)

        song.liked_by.remove(user)
        return Response({"message": "You have unliked this song."}, status=status.HTTP_200_OK)

class LikedSongsView(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        return self.request.user.liked_songs.all()
