from django.urls import path
from .views import ToggleFollowArtistView, FollowedArtistsView, FollowedArtistsContent\
    ,ToggleLikeSongView, LikedSongsView

urlpatterns = [
    path('toggle_follow_artist/', ToggleFollowArtistView.as_view(), name='toggle_follow_artist'),
    path('followed_artists/', FollowedArtistsView.as_view(), name='followed_artists'),
    path('followed_content/', FollowedArtistsContent.as_view(), name='followed_content'),
    path('toggle_like_song/', ToggleLikeSongView.as_view(), name='toggle_like_song'),
    path('liked_songs/', LikedSongsView.as_view(), name='liked_songs'),
]