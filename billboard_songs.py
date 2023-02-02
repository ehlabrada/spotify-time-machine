import requests
from bs4 import BeautifulSoup


def get_billboard_songs(url):
    """

    :param url: url where to look in order to get the list of songs
    :return: a list[str] of songs from the given date throughout the url
    """
    # Using request module
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code != 204:
        billboard_html = response.text

    # Creating Soup Object
    soup = BeautifulSoup(billboard_html, parser="html.parser")

    # Getting the songs names
    songs_h3 = soup.select(selector="li ul li h3.c-title")
    songs = [song.getText().strip() for song in songs_h3]

    return songs

















