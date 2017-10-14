import pygame,os
import random
from threading import Thread
import songmeta

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

class newthread(Thread):
    def __init__(self):
        Thread.__init__(self)
        #self.threadname=name
    def setob(self,ob):
        self.ob=ob
    def run(self):
        playmusic(self.ob)

def playmusic(ob):
    global stoptag,previoustag,pausedtag,nexttag,index,pbusy
    stoptag = 0
    previoustag = 0
    pausedtag = 0
    nexttag = 0

    #index = 0

    pygame.mixer.init()
    pygame.display.init()
    end = pygame.USEREVENT + 1

    pygame.mixer.music.set_endevent(end)

    pygame.mixer.music.load(files[index])

    print("loaded")

    print pygame.mixer.music.get_pos()

    pygame.mixer.music.play()

    print(pygame.mixer.music.get_volume())

    ob.updateval(index)

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
                pygame.mixer.music.load(files[index])
                ob.updateval(index)
                print(files[index])
                print 'im here'
                pygame.mixer.music.play()

                continue
            elif(previoustag == 1):
                if(index>0):
                    print "it should go back"
                    index = index-1
                    pygame.mixer.music.load(files[index])
                    print(files[index])
                    ob.updateval(index)
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    continue
                else:
                    print "it should rewind"
                    pygame.mixer.music.rewind()
                    print(files[index])
                    ob.updateval(index)
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    continue
            else:

                pygame.mixer.music.stop()
                print "it should stop"
                print "song ended"
                print(index)
                pbusy=False
                exit(False)

        for event in pygame.event.get():
            if event.type == end:
                if index<(len(files)-1):
                    print "it should play next"
                    index = index + 1
                    pygame.mixer.music.load(files[index])
                    print(files[index])
                    ob.updateval(index)
                    pygame.mixer.music.play()
                print "song ends event"


def getmeta():
    global metadata
    return metadata

def getindex():
    global index
    return index
def getlist(*args):
    global index
    index = 0
    global metadata
    if(len(args)==0):
        music_link = 'C:/Users/Harshit Soni/Desktop/python/forProject/'
    else:
        music_link = args[0]
        for filename in os.listdir(music_link):
            if filename.endswith(".mp3"):
                files.append(music_link + filename)
                metadata.append(songmeta.music(music_link + filename))
    print files

def play(screenob):
    global stoptag, previoustag, pausedtag, nexttag
    stoptag = 0
    previoustag = 0
    pausedtag = 0
    nexttag = 0
    print index
    print files
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
    global stoptag, nexttag

    nexttag = 0
    global previoustag
    previoustag = 1
    stoptag = 1
    #pygame.mixer.music.stop()

def playselected():
    pass

def shuffleandplay():
    global files
    random.shuffle(files)
    play()