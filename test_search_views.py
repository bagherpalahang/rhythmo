import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.search.models import SearchQuery

@pytest.mark.django_db
def test_search_api():
    client = APIClient()
    url = reverse("search")
    data = {"query": "test song"}
    response = client.get(url, data)
    assert response.status_code == 200
    assert SearchQuery.objects.filter(query_text="test song").exists()