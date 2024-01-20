import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_id ='' #client ID
client_secret = '' #client secret

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(lz_uri)

# 曲を再生
spotify.start_playback(uris=[lz_uri])