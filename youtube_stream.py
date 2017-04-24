import pafy, pyglet
import urllib.request
from urllib.parse import *
from bs4 import BeautifulSoup


class Youtube_mp3():
    def __init__(self):
        self.lst = []
        self.dict = {}
        self.dict_names = {}
        self.playlist = []

    def url_search(self, search_string, max_search):
        textToSearch = search_string
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        i = 1
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            if len(self.dict) < max_search:
                self.dict[i] = 'https://www.youtube.com' + vid['href']
                i += 1
            else:
                break


    def get_search_items(self, max_search):

        if self.dict != {}:
            i = 1
            for url in self.dict.values():
                try:
                    info = pafy.new(url)
                    self.dict_names[i] = info.title
                    print("{0}. {1}".format(i, info.title))
                    i += 1

                except ValueError:
                    pass

    def play_media(self, num):
        url = self.dict[int(num)]
        info = pafy.new(url)
        #audio = info.m4astreams[-1]
        audio = info.getbestaudio(preftype="m4a")
        audio.download('song.m4a', quiet=True)
        song = pyglet.media.load('song.m4a')
        player = pyglet.media.Player()
        player.queue(song)
        print("Playing: {0}.".format(self.dict_names[int(num)]))
        player.play()
        stop = ''
        while True:
            stop = input('Type "s" to stop; "p" to pause; "" to play; : ')
            if stop == 's':
                player.pause()
                break
            elif stop == 'p':
                player.pause()
            elif stop == '':
                player.play()
            elif stop == 'r':
                #player.queue(song)
                #player.play()
                print('Replaying: {0}'.format(self.dict_names[int(num)]))
                




    def download_media(self, num):
        url = self.dict[int(num)]
        info = pafy.new(url)
        audio = info.getbestaudio(preftype="m4a")
        song_name = self.dict_names[int(num)]
        print("Downloading: {0}.".format(self.dict_names[int(num)]))
        print(song_name)
        song_name = input("Filename (Enter if as it is): ")
 #       file_name = song_name[:11] + '.m4a'
        file_name = song_name + '.m4a'
        if song_name == '':
            audio.download(remux_audio=True)
        else:
            audio.download(filepath = filename, remux_audio=True)


    def bulk_download(self, url):
        info = pafy.new(url)
        audio = info.getbestaudio(preftype="m4a")
        song_name = self.dict_names[int(num)]
        print("Downloading: {0}.".format(self.dict_names[int(num)]))
        print(song_name)
        song_name = input("Filename (Enter if as it is): ")
 #       file_name = song_name[:11] + '.m4a'
        file_name = song_name + '.m4a'
        if song_name == '':
            audio.download(remux_audio=True)
        else:
            audio.download(filepath = filename, remux_audio=True)

    def add_playlist(self, search_query):
        url = self.url_search(search_query, max_search=1)
        self.playlist.append(url)





if __name__ == '__main__':
    print('Welcome to the Youtube-Mp3 player.')
    x = Youtube_mp3()
    search = ''
    while search != 'q':
        search = input("Youtube Search: ")
        old_search = search
        max_search = 5
        # if search == '':
        #     print('\nFetching for: {0} on youtube.'.format(old_search.title()))
        #     x.url_search(search, max_search)
        #     x.get_search_items(max_search)
        #     song_number = input('Input song number: ')
        #     x.play_media(song_number)

        x.dict = {}
        x.dict_names = {}

        if search == 'q':
            print("Ending Youtube-Mp3 player.")
            break

        download = input('1. Play Live Music\n2. Download Mp3 from Youtube.\n')
        if search != 'q' and (download == '1' or download == ''):
            print('\nFetching for: {0} on youtube.'.format(search.title()))
            x.url_search(search, max_search)
            x.get_search_items(max_search)
            song_number = input('Input song number: ')
            x.play_media(song_number)
        elif download == '2':
            print('\nDownloading {0} (conveniently) from youtube servers.'.format(search.title()))
            x.url_search(search, max_search)
            x.get_search_items(max_search)
            song_number = input('Input song number: ')
            x.download_media(song_number)
#github commit
