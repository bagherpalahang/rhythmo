import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_homepage():
    client = APIClient()
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200

def test_api_status():
    client = APIClient()
    url = reverse("api-root")
    response = client.get(url)
    assert response.status_code == 200