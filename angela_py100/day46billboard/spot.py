import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

spotify_app_client_id = os.environ["SPOTIFY_APP_CLIENT_ID"]
spotify_app_client_secret = os.environ["SPOTIFY_APP_CLIENT_SECRET"]
spotify_app_client_redirect_uri = os.environ["SPOTIFY_APP_REDIRECT_URI"]

scope = ["user-library-read", "playlist-modify-private"]
#scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=
    SpotifyOAuth(
        client_id=spotify_app_client_id,
        client_secret=spotify_app_client_secret,
        redirect_uri=spotify_app_client_redirect_uri,
        show_dialog=True,
        cache_path="token.txt",
        scope=scope ))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
#
# pprint(results)

#ret = sp.user_playlist_create(user="sunpochin", name="billboard",  description="100 billboard")
#pprint(ret)
user_id = sp.current_user()["id"]
print("\n user: ", user_id)
ret = sp.user_playlist_create(
    user=user_id,
    name="billboard",
    description="100 billboard",
    public=False)
