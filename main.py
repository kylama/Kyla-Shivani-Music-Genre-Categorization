# html libraries
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

import pickle
import numpy as np
import pandas as pd

# Spotify API libraries
from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
  auth_string = str(client_id) + ":" + str(client_secret)
  auth_bytes = auth_string.encode("utf-8")
  auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
  
  url = "https://accounts.spotify.com/api/token"
  headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded"
  }
  data = {"grant_type": "client_credentials"}
  result = post(url, headers = headers, data = data)
  print(result)
  json_result = json.loads(result.content)
  print(json_result)
  token = json_result["access_token"]
  return token

def get_auth_header(token):
  return {"Authorization": "Bearer " + token}

def search_for_song(song, artist):
  token = get_token()
  url = "https://api.spotify.com/v1/search"
  headers = get_auth_header(token)
  query = f"?q={song}{artist}&type=track&limit=1"

  query_url = url + query
  result = get(query_url, headers = headers)
  json_result = json.loads(result.content)
  return(json_result)

def get_audio_features(song_id):
  token = get_token()
  headers = get_auth_header(token)
  query_url = f"https://api.spotify.com/v1/audio-features/{song_id}"
  result = get(query_url, headers = headers)
  json_result = json.loads(result.content)
  data = pd.DataFrame([json_result])
  return data

@app.route('/')
def render_home():
    return render_template('home.html')

@app.route('/song_result', methods=['POST'])
def categorize():
  input_song = find_song(request.form['song'], request.form['artist'])
  genre_result = num_to_genre(lr.predict(input_song))
  input_song_id = find_id(request.form['song'], request.form['artist'])
  return render_template('song_result.html', genre = genre_result, id = input_song_id)

genre_list = np.array(['pop', 'hip hop', 'rock', 'country', 'metal', 'R&B', 'Dance/Electronics', 'Folk/Acoustic', 'latin', 'blues', 'easy listening', 'jazz', 'World/Traditional', 'classical', 'none'])
def num_to_genre(holder: int) -> str:
  """Takes a number and returns a genre."""
  genre_string = np.array2string(genre_list[holder - 1])
  return genre_string[2:-2]

# load saved model
with open('model_pkl' , 'rb') as f:
  lr = pickle.load(f)

def find_song(song, artist):
    song_result = search_for_song(song, artist)
    id = song_result.get('tracks').get("items")[0].get("id")
    song_data = get_audio_features(id)
    
    danceability = song_data['danceability']
    energy = song_data['energy']
    key = song_data['key']
    loudness = song_data['loudness']
    speechiness = song_data['speechiness']
    acousticness = song_data['acousticness']
    instrumentalness = song_data['instrumentalness']
    liveness = song_data['liveness']
    valence = song_data['valence']
    tempo = song_data['tempo']

    new_song_data = np.array([danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo])
    new_song_data = new_song_data.reshape(1,-1)
    print(new_song_data.shape)
    return new_song_data

def find_id(song, artist):
    song_result = search_for_song(song, artist)
    return song_result.get('tracks').get("items")[0].get("id")

if __name__ == "__main__":
   app.run(host='0.0.0.0')
