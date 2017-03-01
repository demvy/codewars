__author__ = 'valeriy'
song = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"


def song_decoder(song):
    return ' '.join(word for word in song.split('WUB') if word != '')

#a = song_decoder(song)


def f(n):
    if isinstance(n, int) and n > 0:
        return (2 + n - 1)*n/2
    else:
        return None

a = f(100)
print(a)