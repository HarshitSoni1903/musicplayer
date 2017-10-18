import pygame
import random, requests, time
import moodmusic
#from Tkinter import *
from threading import Thread
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
    global metadata
    return metadata


class newthread(Thread):
    def __init__(self):
        Thread.__init__(self)
        #self.threadname=name
    def setob(self,ob):
        self.ob=ob
    def run(self):
        playmusic(self.ob)

def playmusic(ob):
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
    time.sleep(2)
    pygame.mixer.music.load(r.raw)
    pygame.mixer.music.play()
    ob.updateval(index)

    # pygame.mixer.music.set_pos(190)


    while True:
        if pausedtag == 1:
            continue
        if stoptag == 1:
            if nexttag == 1:
                if(index<len(files)-1):
                    stoptag = 0
                    nexttag = 0
                    index = index + 1
                    pygame.mixer.music.stop()
                    r = requests.get(files[index], stream=True)
                    time.sleep(2)
                    pygame.mixer.music.load(r.raw)
                    pygame.mixer.music.play()
                    ob.updateval(index)
                    continue
                else:
                    continue
            elif(previoustag == 1):
                if(index>0):
                    index = index-1
                    r = requests.get(files[index], stream=True)
                    time.sleep(2)
                    pygame.mixer.music.load(r.raw)
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    ob.updateval(index)
                    continue

                else:
                    pygame.mixer.music.rewind()
                    time.sleep(2)
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    ob.updateval(index)
                    continue
            else:
                pygame.mixer.music.stop()
                exit(False)

        for event in pygame.event.get():
            if event.type == end:
                if index<(len(files)-1):

                    index = index + 1
                    r = requests.get(files[index], stream=True)
                    time.sleep(2)
                    pygame.mixer.music.load(r.raw)
                    getmeta()
                    pygame.mixer.music.play()
                    ob.updateval(index)

def getindex():
    global index
    return index

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

def play(screenob):
    global stoptag, previoustag, pausedtag, nexttag, index
    stoptag = 0
    previoustag = 0
    pausedtag = 0
    nexttag = 0
    ob1 = newthread()
    ob1.setob(screenob)
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