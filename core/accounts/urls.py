from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from .views import RegisterView, ValidateOtpView, ChangeUserData, ChangeUserPassword, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('otp/', ValidateOtpView.as_view(), name='otp'),
    path('change_profile/', ChangeUserData.as_view(), name='change_profile'),
    path('change_password/', ChangeUserPassword.as_view(), name='change_password'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]
