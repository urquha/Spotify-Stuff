
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

from gets import get_all_user_tracks_df, get_user_tracks_df

def main():
    scope = "user-library-read"

    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    # df = get_user_tracks_df(spotify, 52)
    df = get_all_user_tracks_df(spotify)
    # df = df.sort_values('Popularity')
    print(df)



if __name__ == "__main__":
    main()