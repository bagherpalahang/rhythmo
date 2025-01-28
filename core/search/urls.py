from django.urls import path
from .views import GlobalSearchView

urlpatterns = [
    path('<str:query>/', GlobalSearchView.as_view(), name='global_search'),
]