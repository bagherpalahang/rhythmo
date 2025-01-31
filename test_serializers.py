from core.accounts.serializers import UserSerializer
from core.accounts.models import User

def test_user_serializer():
    user = User(username="testuser", email="test@example.com")
    serializer = UserSerializer(instance=user)
    assert serializer.data["username"] == "testuser"
    assert serializer.data["email"] == "test@example.com"