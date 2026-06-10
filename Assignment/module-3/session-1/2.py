f = open(r'E:\Python\Assignment\module-3\session-1\my_fav_songs.txt', 'r')

for i, song in enumerate(f, start=1):
    print(i, song.strip())

