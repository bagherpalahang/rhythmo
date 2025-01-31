@pytest.mark.django_db
def test_get_artist_detail():
    client = APIClient()
    artist = Artist.objects.create(name="Test Artist", genre="Rock")
    
    url = reverse("artist-detail", args=[artist.id])
    response = client.get(url)
    
    assert response.status_code == 200
    assert response.data["name"] == "Test Artist"