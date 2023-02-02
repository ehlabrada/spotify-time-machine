import billboard_songs
from security_access import SpotifyAPI


YEAR, MONTH, DAY = input("Which year do you want to travel to? Type the date "
                         "in this format YYYY-MM-DD: ").split("-")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{YEAR}-{MONTH}-{DAY}/"


# Getting the songs
songs = billboard_songs.get_billboard_songs(BILLBOARD_URL)

# Configure access to spotify
sp = SpotifyAPI()

# Create playlist
# playlist_date = f"{2000}-{12}-{12}"
playlist_date = f"{YEAR}-{MONTH}-{DAY}"
generated_playlist_name = f"{playlist_date} Billboard 100"
sp.create_playlist(generated_playlist_name)

# Get playlist URI

# Add songs to the playlist
sp.add_songs_to_playlist(songs, generated_playlist_name)







































