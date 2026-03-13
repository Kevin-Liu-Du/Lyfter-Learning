class Playlist():
    def __init__(self, name):
        self.name = name
        self.songs_list = []

    def add_songs(self, song):
        self.songs_list.append(song)
        print(f"{song} added to the playlist. ")

    def remove_song(self, song):
        if song in self.songs_list:
            self.songs_list.remove(song)
            print(f"{song} deleted from the playlist.")
        else:
            print(f"The song '{song}' not found. ")

    def show_songs(self):
        print(f"The Playlist: {self.name}")
        for index, song in enumerate(self.songs_list, start=1):
            print(f"{index}: {song}")


song_a = "x"
song_b = "m"
song_c = "K"
song_d = "Hello"


playlist = Playlist('My Favorites')
playlist.add_songs(song_a)
playlist.add_songs(song_b)
playlist.add_songs(song_c)

playlist.show_songs()

playlist.remove_song(song_d)
playlist.remove_song(song_a)

playlist.show_songs()


