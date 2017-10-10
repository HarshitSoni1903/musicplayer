import threading
import new1
import Tkinter as tk
import initfile
import pygame

class newthread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.threadname=name
    def run(self):
        if(self.threadname=="Hello"):
            new1.play1()
        if(self.threadname=="hi"):
            new1.play2()

class gui:
    def __init__(self,master):
        framei = tk.Frame(master)
        framei.pack()
        self.button1 = tk.Button(framei, text="Play", command=self.startthread)
        self.button2 = tk.Button(framei, text="Play2", command=self.globalthread)
        self.button3 = tk.Button(framei, text="Play3", command=self.resumethread)
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def startthread(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Down.mp3")
        ob1 = newthread("Hello")
        ob2 = newthread("hi")
        ob1.start()
        ob2.start()

    def globalthread(self):
        initfile.paused=1

    def resumethread(self):
        initfile.resume=1


root = tk.Tk()
ob = gui(root)
root.mainloop()
