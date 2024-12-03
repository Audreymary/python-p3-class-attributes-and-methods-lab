class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment count of songs
        Song.add_song_to_count()
        
        # Add to genres, artists, and update counts
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the song count when a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds the genre to the genres list if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds the artist to the artists list if it's not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates the genre_count dictionary with the number of songs per genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates the artist_count dictionary with the number of songs per artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Hotline Bling", "Drake", "Pop")
song3 = Song("Halo", "Beyoncé", "Pop")
song4 = Song("Empire State of Mind", "Jay-Z", "Rap")
song5 = Song("Single Ladies", "Beyoncé", "Pop")

# Accessing the class attributes
print(Song.count)  # Total song count
print(Song.artists)  # List of unique artists
print(Song.genres)  # List of unique genres
print(Song.genre_count)  # Histogram of genre counts
print(Song.artist_count)  

