from django.urls import path
from .views import ToggleFollowArtistView, FollowedArtistsView, FollowedArtistsContent\
    ,LikeSongView, UnlikeSongView, LikedSongsView

urlpatterns = [
    path('toggle_follow_artist/', ToggleFollowArtistView.as_view(), name='toggle_follow_artist'),
    path('followed-artists/', FollowedArtistsView.as_view(), name='followed_artists'),
    path('followed-content/', FollowedArtistsContent.as_view(), name='followed_content'),
    path('songs/<int:song_id>/like/', LikeSongView.as_view(), name='like_song'),
    path('songs/<int:song_id>/unlike/', UnlikeSongView.as_view(), name='unlike_song'),
    path('liked-songs/', LikedSongsView.as_view(), name='liked_songs'),
]