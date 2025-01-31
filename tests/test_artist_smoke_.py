import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_artists_list():
    client = APIClient()
    url = reverse("artist-list")
    response = client.get(url)
    assert response.status_code == 200

def test_artists_endpoint_available():
    client = APIClient()
    url = reverse("artist-list")
    response = client.options(url)
    assert response.status_code == 200