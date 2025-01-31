import json
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .serializers import ArtistSerializer, SongSerializer, AlbumSerializer, ArtistDetailSerializer
from .models import Artist, Song, Album

# Create your views here.

class ToggleFollowArtistView(APIView):
    permission_classes = [IsAuthenticated]    

    def post(self, request):

        json_data = json.loads(request.body)
        artist_id = int(json_data['artist_id'])

        artist = get_object_or_404(Artist, id=artist_id)
        user = request.user

        if user in artist.followers.all():
            artist.followers.remove(user)
            return Response({"message": "You have unfollowed this artist."}, status=status.HTTP_200_OK)
        else:
            artist.followers.add(user)
            return Response({"message": "You are now following this artist."}, status=status.HTTP_200_OK)

class CheckFollowArtistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        is_following = artist.followers.filter(id=request.user.id).exists()
        return Response({'is_following': is_following})

class FollowedArtistsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_artists = request.user.following_artists.all() 
        serializer = ArtistSerializer(followed_artists, many=True)  
        return Response(serializer.data)

class FollowedArtistsContent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user
        followed_artists = user.following_artists.all()

        songs = Song.objects.filter(artist__in=followed_artists).order_by('-created_at')
        albums = Album.objects.filter(artist__in=followed_artists).order_by('-release_date')

        song_serializer = SongSerializer(songs, many=True, context={'request': request})
        album_serializer = AlbumSerializer(albums, many=True)

        combined_results = sorted(
            song_serializer.data + album_serializer.data,
            key=lambda x: x.get('created_at', x.get('release_date')),
            reverse=True
        )

        return Response(combined_results, status=200)

class ToggleLikeSongView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        json_data = json.loads(request.body)
        song_id = int(json_data['song_id'])

        song = get_object_or_404(Song, id=song_id)
        user = request.user

        if user in song.liked_by.all():
            song.liked_by.remove(user)
            return Response({"message": "You have unliked this song."}, status=status.HTTP_200_OK)
        else:
            song.liked_by.add(user)
            return Response({"message": "You have liked this song."}, status=status.HTTP_200_OK)

class LikedSongsView(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        return self.request.user.liked_songs.all()

class AlbumSongsView(generics.ListAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        return Song.objects.filter(album_id=album_id)

class ArtistDetailView(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer
