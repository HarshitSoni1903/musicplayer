import pygame,os
import threading,random

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

class newthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.threadname=name
    def run(self):
        playmusic()

def playmusic():
    global stoptag,previoustag,pausedtag,nexttag,index
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
                pygame.mixer.music.load(files[index])
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
                    pygame.mixer.music.play()
                    stoptag = 0
                    previoustag = 0
                    continue
                else:
                    print "it should rewind"
                    pygame.mixer.music.rewind()
                    print(files[index])
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
                    pygame.mixer.music.load(files[index])
                    print(files[index])
                    pygame.mixer.music.play()
                print "song ends event"


def getlist(*args):
    global index
    index = 0
    if(len(args)==0):
        music_link = 'C:/Users/Harshit Soni/Desktop/python/forProject/'
    else:
        music_link = args[0]
        for filename in os.listdir(music_link):
            if filename.endswith(".mp3"):
                files.append(music_link + filename)
    print files

def play():
    global stoptag, previoustag, pausedtag, nexttag
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