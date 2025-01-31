# Rhythmo

## Overview
Music Stream App is a Flutter and Django-based music streaming platform that allows users to create accounts, follow artists, search for albums, songs, and artists, and listen to their favorite tracks.

## Features
- **User Authentication**: Sign up, log in, and manage your account.
- **Follow Artists**: Stay updated with your favorite artists.
- **Search Functionality**: Find albums, songs, and artists with ease.
- **Edit Profile**: Customize your user profile.
- **Music Streaming**: Listen to songs directly from the app.

## Tech Stack
- **Frontend**: Flutter (Dart)
- **Backend**: Django (Python)
- **Database**: SQLite
- **API Communication**: REST API with Django REST Framework

## Installation

### Backend (Django)
1. Clone the repository:
   ```sh
   git clone https://github.com/bagherpalahang/rhythmo.git
   cd core
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations and start the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend (Flutter)
1. Navigate to the frontend directory:
   ```sh
   cd ../rhythmo_mobile
   ```
2. Install Flutter dependencies:
   ```sh
   flutter pub get
   ```
3. Run the app:
   ```sh
   flutter run
   ```

## API Endpoints
- Accounts
- POST `/accounts/register/` - Register a new user
- POST `/accounts/login/` - Authenticate user
- POST `/accounts/otp/` - Validate OTP
- POST `/accounts/change_profile/` - Change user profile
- POST `/accounts/change_password/` - Change user password
- GET `/accounts/user/` - Get user details

- Artists
- POST `/artists/toggle_follow_artist/` - Follow/unfollow an artist
- GET `/artists/followed_artists/` - Get followed artists
- GET `/artists/followed_content/` - Get content from followed artists
- POST `/artists/toggle_like_song/` - Like/unlike a song
- GET `/artists/liked_songs/` - Get liked songs
- GET `/artists/albums/<album_id>/songs/` - Get songs from an album
- GET `/artists/<pk>/detail/` - Get artist details
- GET `/artists/<artist_id>/is_following/` - Check if user is following an artist

- Search
- GET `/search/<str:query>/` - Global search for artists, albums, and songs

## Contribution
Feel free to contribute to this project by submitting issues or pull requests!

## License
This project is licensed under the MIT License.

---
Happy Coding! 🎵

