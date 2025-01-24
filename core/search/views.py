from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from artists.models import Artist, Album, Song
from artists.serializers import ArtistSerializer, AlbumSerializer, SongSerializer

# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class GlobalSearchView(APIView):
    pagination_class = CustomPagination

    def get(self, request):
        query = request.query_params.get('q', '').strip()

        if not query:
            return Response([])
        
        results = []

        artists = Artist.objects.filter(name__icontains=query)
        results.extend(ArtistSerializer(artists, many=True).data)

        albums = Album.objects.filter(title__icontains=query)
        results.extend(AlbumSerializer(albums, many=True).data)

        songs = Song.objects.filter(title__icontains=query)
        results.extend(SongSerializer(songs, many=True, context={'request': request}).data)

        paginator = self.pagination_class()
        paginated_results = paginator.paginate_queryset(results, request)

        return paginator.get_paginated_response(paginated_results)