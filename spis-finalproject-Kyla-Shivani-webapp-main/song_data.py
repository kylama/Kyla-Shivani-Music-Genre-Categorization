import pandas as pd
import numpy as np
import main
from spotipy.oauth2 import SpotifyClientCredentials

# def find_song(song, artist):
#     song_result = main.search_for_song(song, artist)
#     id = song_result.get('tracks').get("items")[0].get("id")
#     song_data = main.get_audio_features(id)
#     #song_data = song_data.drop(['analysis_url', 'duration', 'id', 'mode', 'time_signature', 'track_href', 'type', 'uri'])
#     danceability = song_data['danceability']
#     energy = song_data['energy']
#     key = song_data['key']
#     loudness = song_data['loudness']
#     speechiness = song_data['speechiness']
#     acousticness = song_data['acousticness']
#     instrumentalness = song_data['instrumentalness']
#     liveness = song_data['liveness']
#     valence = song_data['valence']
#     tempo = song_data['tempo']

#     new_song_data = np.array([[danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo]])
#     return new_song_data