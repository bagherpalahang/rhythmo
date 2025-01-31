import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from core.accounts.models import User

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    url = reverse("register")
    data = {"username": "newuser", "email": "new@example.com", "password": "securepass"}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert User.objects.filter(username="newuser").exists()
