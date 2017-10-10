import pygame
import requests


test=["https://ia800208.us.archive.org/8/items/FixYou_201601/Fix%20you.mp3"]
#test.append(str(raw_input("enter link")))

pygame.mixer.init()

pygame.display.init()

end = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(end)

index =0

global i
i=0

def play(index):

    global i

    r=requests.get(test[index],stream=True)

    pygame.mixer.music.load(r.raw)

    pygame.mixer.music.play()
    while True:

        for event in pygame.event.get():
            if event.type == end:
                if (index < len(test)-1):
                    index=index+1
                    print "song ends"
                    play(index)

                else:
                    index=0
                    print("ended")
                    play(index)

play(index)
