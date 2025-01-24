from django.urls import path
from .views import FollowArtistView, UnfollowArtistView, FollowedArtistsView, FollowedArtistsContent  

urlpatterns = [
    path('artists/<int:artist_id>/follow/', FollowArtistView.as_view(), name='follow_artist'),
    path('artists/<int:artist_id>/unfollow/', UnfollowArtistView.as_view(), name='unfollow_artist'),
    path('followed-artists/', FollowedArtistsView.as_view(), name='followed_artists'),
    path('followed-content/', FollowedArtistsContent.as_view(), name='followed_content'),
]