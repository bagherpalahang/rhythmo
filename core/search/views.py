import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from artists.models import Artist, Album, Song
from artists.serializers import ArtistSerializer, AlbumSerializer, SongSerializer

# Create your views here.

class GlobalSearchView(APIView):
    def get(self, request, query):

        query = query.lower()
         
        if not query or len(query) <= 3:
            return Response([])
        
        results = {
            'songs' : None,
            'artists' : None,
            'albums' : None
        }

        artists = Artist.objects.filter(name__icontains=query)
        results['artists'] = ArtistSerializer(artists, many=True).data

        albums = Album.objects.filter(title__icontains=query)
        results['albums'] = AlbumSerializer(albums, many=True).data

        songs = Song.objects.filter(title__icontains=query)
        results['songs'] = SongSerializer(songs, many=True, context={'request': request}).data

        print(results)
        return Response(results)