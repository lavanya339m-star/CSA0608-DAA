def insert_song(playlist, new_song):
    playlist.append(new_song)
    i = len(playlist) - 2
    while i >= 0 and playlist[i][1] > new_song[1]:
        playlist[i + 1] = playlist[i]
        i -= 1
    playlist[i + 1] = new_song    return playlist
playlist = [
    ('Intro', 120),
    ('Chill Beat', 210),
    ('Long Jam', 340)
]
updated_playlist = insert_song(playlist, ('Quick Track', 180))
durations = [s[1] for s in updated_playlist]
assert durations == sorted([120, 210, 340, 180])
assert ('Quick Track', 180) in updated_playlist
print("All test cases passed!")
print("Updated playlist:", updated_playlist)
