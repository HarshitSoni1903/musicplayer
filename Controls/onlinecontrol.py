import pygame
import threading,random, requests, time
import moodmusic
from Tkinter import *
from database import getmusiclist
global pausedtag

pausedtag = 0

global stoptag

stoptag = 0

global nexttag

nexttag = 0

global index

index = 0

global previoustag

previoustag = 0

global files

files = []

global metadata

metadata = []

global artist,songname, album,genre


artist = None
album = None
genre = None
songname = None

def getmeta():

    global artist, songname, album, genre,index
    print("inside getmeta")

    """artist = metadata[index][1]
    songname = metadata[index][0]
    album = metadata[index][3]
    genre = metadata[index][2]
    artist = StringVar()
    songname = StringVar()
    album = StringVar()
    genre = StringVar()
    artist.set(metadata[index][1])
    album.set(metadata[index][3])
    genre.set(metadata[index][2])
    songname.set(metadata[index][0])
    print artist"""

    metadict = {'artist': metadata[index][1],'songname' : metadata[index][0],'album' : metadata[index][3],'genre' : metadata[index][2]}

    return metadict
class newthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.threadname=name
    def run(self):
        playmusic()


def playmusic():
    if files==None:
        getlist()
    global stoptag,previoustag,pausedtag,nexttag,index
    stoptag = 0
    previoustag = 0
    pausedtag = 0
    nexttag = 0
    pygame.mixer.init()
    pygame.display.init()
    end = pygame.USEREVENT + 1

    pygame.mixer.music.set_endevent(end)


    r = requests.get(files[index], stream=True)
    getmeta()
    pygame.mixer.music.load(r.raw)
    time.sleep(2)
    pygame.mixer.music.play()

    print(pygame.mixer.music.get_volume())

    # pygame.mixer.music.set_pos(190)

    print pygame.mixer.music.get_pos()

    while True:

        if pausedtag == 1:
            continue

        if stoptag == 1:
            if nexttag == 1:
                print "it should go next"
                stoptag = 0
                nexttag = 0
                index = index + 1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[index])
                print(files[index])
                print 'im here'
                time.sleep(2)
                pygame.mixer.music.play()
                continue
            elif(previoustag == 1):
                if(index>0):
                    print "it should go back"
                    index = index-1
                    pygame.mixer.music.load(files[index])
                    print(files[index])
                    time.sleep(2)
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    continue
                else:
                    print "it should rewind"
                    pygame.mixer.music.rewind()
                    print(files[index])
                    time.sleep(2)
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    continue
            else:
                pygame.mixer.music.stop()
                print "it should stop"
                print "song ended"
                print(index)
                exit(False)

        for event in pygame.event.get():
            if event.type == end:
                if index<(len(files)-1):
                    print "it should play next"
                    index = index + 1
                    r = requests.get(files[index], stream=True)
                    pygame.mixer.music.load(r.raw)
                    getmeta()
                    print(files[index])
                    time.sleep(2)
                    pygame.mixer.music.play()
                print "song ends event"


def getlist():

    global index
    index=0
    mood = moodmusic.findmood()
    musicobj = getmusiclist.getmusiclist(mood)
    music_link = musicobj.getlist()
    #music_link = 'C:/Users/Harshit Soni/Desktop/python/forProject/'
    global metadata

    for link in music_link:
        files.append(link[0])
        metadata.append(link[1:])
    getmeta()
    print files
    print metadata

def play():
    global stoptag, previoustag, pausedtag, nexttag, index
    stoptag = 0
    previoustag = 0
    pausedtag = 0
    nexttag = 0
    print index
    print files
    ob1 = newthread()
    ob1.start()

def pause():
    pygame.mixer.music.pause()
    global pausedtag
    pausedtag = 1


def resume():
    pygame.mixer.music.unpause()
    global pausedtag
    pausedtag = 0


def stop():
    global stoptag
    global nexttag,previoustag
    nexttag = 0
    previoustag = 0
    stoptag = 1
    #pygame.mixer.music.stop()


def nextsong():
    global stoptag
    global nexttag
    stoptag = 1
    nexttag = 1
    #pygame.mixer.music.stop()

def previous():
    global stoptag, nexttag, previoustag

    nexttag = 0
    previoustag = 1
    stoptag = 1
    #pygame.mixer.music.stop()

def playselected():
    pass

def shuffleandplay():
    global files

    random.shuffle(files)
    play()