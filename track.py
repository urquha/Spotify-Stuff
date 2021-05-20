class track:
    num_of_tracks = 0

    def __init__(self, name, artist, album, popularity) -> None:
        self.name = name
        self.artist = artist
        self.album = album
        self.popularity = popularity

    def df_row(self):
        return {'Song_Name': self.name, 'Artist': self.artist, 'Album': self.album, 'Popularity': self.popularity}
