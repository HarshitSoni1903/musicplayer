import pygame
import requests

test="http://dl.taksedaclub.ir/download/1393/10/Taylor%20Swift%20-%20Blank%20Space%20(Gibs%20Ft.%20Noize%20Remix%202015)%20[320].mp3"

pygame.mixer.init()

pygame.display.init()

end = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(end)

r=requests.get(test,stream=True)

pygame.mixer.music.load(r.raw)

pygame.mixer.music.play()
i=0
while (i!=1):
    i=int(input("number"))
print pygame.mixer.music.get_pos()
pygame.mixer.music.pause()
i=0
while (i!=1):
    i=int(input("number"))

pygame.mixer.music.unpause()
i=0
while (pygame.mixer.music.get_busy()):
    i=int(input("number"))
    if(i==1):
        break
print pygame.mixer.music.get_pos()
