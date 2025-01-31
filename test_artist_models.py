import pytest
from core.artists.models import Artist

@pytest.mark.django_db
def test_create_artist():
    artist = Artist.objects.create(name="Test Artist", genre="Rock")
    assert artist.name == "Test Artist"
    assert artist.genre == "Rock"