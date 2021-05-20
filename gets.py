import pandas as pd

def get_tracks(spotify, limit, offset):
    return spotify.current_user_saved_tracks(limit=limit, offset=offset)

def get_all_user_tracks_df(spotify):
    return get_user_tracks_df(spotify, limit=100000)

def get_user_tracks_df(spotify, limit):
    # Track index to get
    offset = 0
    # How many tracks to get each iteration
    jump = 50

    df = pd.DataFrame(columns=['Song_Name', 'Artist', 'Popularity'])

    while True:
        # If theres less than 50 less than the limit, the jump needs to be less than 50 
        if offset + jump > limit:
            jump = limit - offset
        
        results = get_tracks(spotify, jump, offset)

        if len(results['items']) == 0:
            break

        for item in results['items']:
            track = item['track']
            new_row = {'Song_Name': track['name'], 
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'], 
            'Album_Release_Date': track['album']['release_date'], 
            'Album_Total_Tracks': track['album']['total_tracks'], 
            'Popularity': track['popularity']}
            df = df.append(new_row, ignore_index=True)
        
        if jump != 50:
            break

        offset += 50
    
    return df