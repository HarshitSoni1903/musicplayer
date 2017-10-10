import initfile
from Tkinter import *
import pygame
import threading


class newthread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.threadname=name
    def run(self):
        initfile.play()


class simpleui:

    def __init__(self, master):
        self.framei=Frame(master)
        self.framei.pack()
        self.button1 = Button(self.framei, text="play", command=self.play)
        self.button2 = Button(self.framei, text="pause", command=self.pause)
        self.button3 = Button(self.framei, text="stop", command=self.stop)
        self.button4 = Button(self.framei, text="resume", command=self.resume)
        self.button5 = Button(self.framei, text="next", command=self.nextsong)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        var = "harshit"
        self.label = Label(self.framei, text = "Hello "+var+" how are you?")
        self.label.pack()

    def play(self):
        ob1 = newthread()
        ob1.start()

    def pause(self):
        pygame.mixer.music.pause()
        global paused
        paused = 1

    def resume(self):
        pygame.mixer.music.unpause()
        global paused
        paused=0

    def stop(self):
        pygame.mixer.music.stop()
        global stop
        stop = 1

    def nextsong(self):
        pygame.mixer.music.stop()
        global stop
        global next
        stop = 1
        next=1

root = Tk()
songapp = simpleui(root)
root.mainloop()