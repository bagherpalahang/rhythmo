from core.artists.serializers import ArtistSerializer
from core.artists.models import Artist

def test_artist_serializer():
    artist = Artist(name="Test Artist", genre="Rock")
    serializer = ArtistSerializer(instance=artist)
    assert serializer.data["name"] == "Test Artist"
    assert serializer.data["genre"] == "Rock"