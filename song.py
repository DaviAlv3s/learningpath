class Song:
    """Class to represent a song
    Atributes :
        title(str): Title of the song
        artist(Artist): An artist object representing the songs creator
        duration(int): The duration of the song in seconds. may be zero
        """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an Album, using it's track list

    Attributes:
        name (str): The name of the album.
        year (int): The year was album released.
        artist (Artist): The Artist responsible for the album.
            If not specified, the artist will default to an artist
            with the name "Various Artists"
        tracks (List[song]): A list of the songs in the album.

    Methods:
        add_song: Used to add a new song to the album's track list.
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.tracks = []
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
             song(Song): A song to add.
             position(int)(optional): If specified, the song will be
              add that position in the tracklist - inserting in between
              other songs if necessary, Otherwise will be added to the
              end of the list
             """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Atributes:
        name (str): The nem of the artist.
        albums(list[album]): A list of the albums by the artist.
            The list includes only those albums in the collection,it is
            not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list'
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
             album (Album): Album object to add to the list.
                If the album is already added, it will not be added again
                (although this is yet implemented)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (Artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()
