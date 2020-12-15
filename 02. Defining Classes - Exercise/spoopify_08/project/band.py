from spoopify_08.project.album import Album
from spoopify_08.project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: list = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [album.name for album in self.albums]:
            return f"Album {album_name} is not found."

        album = [album for album in self.albums if album.name == album_name][0]
        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        album_details = "\n".join([album.details() for album in self.albums])
        return f"Band {self.name}\n" \
               f"{album_details}"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())

album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())

band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())