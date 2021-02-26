def make_album(artist, title, num_songs=None):
    album_dict = {"artist_name": artist, "album_title": title}
    if num_songs:
        album_dict["num_songs"] = num_songs
    return album_dict


print(make_album("Tom", "Music Stuffs"))
print(make_album("Ted", "Drum Beats"))
print(make_album("Fran", "Kevin's Love Songs", 4078))
