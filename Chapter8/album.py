def MakeAlbum(artist, title, songNum = 'Unknown'):
    album = {'artist': artist, 'title': title, 'number of songs': songNum}
    return album

UserFlag = True
while UserFlag:
    title = input('Album title: ')
    artist = input('Album artist: ')
    songNum = input('Album song number: ')
    print(MakeAlbum(artist, title, songNum))
    userRes = input('Continue? Press "y" if not.')
    if userRes == 'y':
        UserFlag = False

print(MakeAlbum('Talking Heads', 'Remain in Light'))
print(MakeAlbum('Depeche Mode', 'Black Celebration'))
print(MakeAlbum('Depeche Mode', 'Construction Time Again'))
print(MakeAlbum('Ryuichi Sakamoto', 'async', '14'))