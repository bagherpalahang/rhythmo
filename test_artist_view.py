import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.artists.models import Artist

@pytest.mark.django_db
def test_create_artist_api():
    client = APIClient()
    url = reverse("artist-list")
    data = {"name": "New Artist", "genre": "Pop"}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert Artist.objects.filter(name="New Artist").exists()