@pytest.mark.django_db
def test_user_login():
    client = APIClient()
    user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
    
    url = reverse("login")
    response = client.post(url, {"username": "testuser", "password": "password123"}, format="json")
    
    assert response.status_code == 200
    assert "token" in response.data