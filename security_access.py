# ENVIROMENT SYSTEM
import os
from dotenv import load_dotenv

import pprint
import json

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()  # take environment variables from .env.

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SPOTIFY_BASE_URL = "https://api.spotify.com/v1/"

class SpotifyAPI:

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID, CLIENT_SECRET,
                                                            redirect_uri="https://example.com",
                                                            scope="playlist-modify-public"))
        self.user_id = self.sp.current_user()["id"]

    # Create playlist
    def create_playlist(self, playlist_name):

        self.sp.user_playlist_create(self.user_id, playlist_name, description="Musical Time Machine")

    def search_songs_uri(self, songs: list):

        uri_songs = []
        for song in songs:
            try:
                uri = self.sp.search(q=f"track: {song}")
            except Exception("Sorry that song it's not available"):
                pass
            else:
                uri_songs.append(uri["tracks"]["items"][0]["uri"])
        return uri_songs

    # Add songs to the playlist
    def add_songs_to_playlist(self, song_list, playlist_name: str):
        """
        :param song_list: list of string-like songs name
        :param playlist_name: name of the playlist where add the songs list
        :return: void
        This function add all the songs from the given list into a playlist
        """

        uri_songs = self.search_songs_uri(song_list)

        user_playlists = self.sp.current_user_playlists()
        playlist_id = user_playlists["items"][0]["uri"]

        # Adds tracks/episodes to a playlist
        self.sp.playlist_add_items(playlist_id, uri_songs)

        return True

