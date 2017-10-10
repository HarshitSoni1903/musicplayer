global paused

paused=0

global stop

stop=0

global next
next = 0

import pygame,os

def play():
    index = 0
    music_link='C:/Users/Harshit Soni/Desktop/python/forProject/'

    files=[]

    for filename in os.listdir(music_link):
        if filename.endswith(".mp3"):
            files.append(music_link+'/'+filename)

    pygame.mixer.init()
    pygame.display.init()
    end = pygame.USEREVENT + 1



    pygame.mixer.music.set_endevent(end)

    pygame.mixer.music.load(files[index])

    print("loaded")

    print pygame.mixer.music.get_pos()

    pygame.mixer.music.play()

    print(pygame.mixer.music.get_volume())

    #pygame.mixer.music.set_pos(190)

    print pygame.mixer.music.get_pos()

    while True:

        if paused == 1:
            continue

        if stop == 1:
            if next==1:
                index=index+1
                pygame.mixer.music.load(files[index])
                pygame.mixer.music.play()
            else:
                print "song ended"
                break

        for event in pygame.event.get():
            if event.type == end:
                index = index + 1
                pygame.mixer.music.load(files[index])
                pygame.mixer.music.play()
                print "song ends"