import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_search_endpoint_available():
    client = APIClient()
    url = reverse("search")
    response = client.get(url)
    assert response.status_code == 200

def test_search_options():
    client = APIClient()
    url = reverse("search")
    response = client.options(url)
    assert response.status_code == 200