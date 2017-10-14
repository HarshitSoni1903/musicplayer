from Tkinter import *
import socket
from Controls import screen2
from gui import offlinescreen, onlinescreen


class secondscreen:

    #if user already in db or has been added
    def __init__(self, master):
        self.master = master
        self.framei = Frame(master)
        #framei["bg"] = "light sky blue"
        self.framei.pack()
        self.button1 = Button(self.framei, text="Play my own Music", command=self.ownmusic)
        self.button2 = Button(self.framei, text="Use camera", command=self.camera1)
        #self.button3 = Button(self.framei, text="Ask me questions", command=self.questions)
        self.text1 = Label(self.framei, text = "This is the very first player to play music online and it uses mood based sentiment analysis")
        self.text2 = Label(self.framei, text = "How would you like to listen to music??")
        self.text3 = Label(self.framei, text = "Can we use camera to select best fit music for you??")
        #self.text4 = Label(self.framei, text = "Not in Mood of a picture? We can ask you questions!")
        self.text5 = Label(self.framei, text = "Have your own Music? No worries, we can play it too!")
        self.text1.grid(row=0, columnspan=4, pady=5)
        self.text2.grid(row=2, columnspan=4, pady=5)
        self.text3.grid(row=3, column=0, columnspan=2, pady=5)
        self.button2.grid(row=4, column =0, columnspan=2)
        #self.text4.grid(row=3, column=2,columnspan=2, pady=5)
        #self.button3.grid(row=4, column=2, columnspan=2)
        self.text5.grid(row=5, column=0, columnspan=4, pady=10)
        self.button1.grid(row=6, column=0, columnspan=4)

    #user chooses to listen to his own choice of music
    def ownmusic(self):
        self.framei.destroy()
        ob = offlinescreen.offlinescreen()
        # print("object created")
        ob.makescreen(self.master, ob)

    #user chooses to use camera to detect mood
    def camera1(self):
        screen2.camera1(socket.gethostname())
        self.framei.destroy()
        print("added to db")
        ob = onlinescreen.onlinescreen()
        # print("object created")
        ob.makescreen(self.master, ob)