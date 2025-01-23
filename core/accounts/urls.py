from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('otp/', views.ValidateOtpView.as_view(), name='otp'),
    path('change_profile/', views.ChangeUserData.as_view(), name='change_profile'),
    path('change_password/', views.ChangeUserPassword.as_view(), name='change_password'),
    path('get_user_data/', views.GetUserData.as_view(), name='get_user_data'),
]
