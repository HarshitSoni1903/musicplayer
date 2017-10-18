from Tkinter import *
import socket
from Controls import screen2
from gui import offlinescreen, onlinescreen


class secondscreen:

    #if user already in db or has been added
    def __init__(self, master):
        self.master = master
        self.framei = Frame(master)
        self.framei["bg"] = "navy blue"
        self.framei.pack()
        self.button1 = Button(self.framei, text="Play my own Music", command=self.ownmusic, font=("Helvetica",14),bg="navy blue", fg="white")
        self.button2 = Button(self.framei, text="Use camera", command=self.camera1, font=("Helvetica",14),bg="navy blue",fg="white")
        master.geometry("320x200")
        master.configure(background="navy blue")
        #self.button3 = Button(self.framei, text="Ask me questions", command=self.questions)
        #self.text1 = Label(self.framei, text = "MOOD ANALYSER", font=("Helvetica",14),bg="powder blue")
        self.text2 = Label(self.framei, text = "How would you like to listen to music?", font=("Helvetica",14),bg="navy blue",fg="white")
        self.text3 = Label(self.framei, text = "Can we click a picture to guess your mood?", font=("Helvetica",14),bg="navy blue",fg="white")
        #self.text4 = Label(self.framei, text = "Not in Mood of a picture? We can ask you questions!")
        self.text5 = Label(self.framei, text = "Have your own Music? No worries, we can play it too!", font=("Helvetica",14),bg="navy blue",fg="white")
        #self.text1.grid(row=0)
        self.text2.grid(row=1)
        self.text3.grid(row=2)
        self.button2.grid(row=3)
        #self.text4.grid(row=3, column=2,columnspan=2, pady=5)
        #self.button3.grid(row=4, column=2, columnspan=2)
        self.text5.grid(row=4)
        self.button1.grid(row=5)

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
        ob = onlinescreen.onlinescreen()
        # print("object created")
        ob.makescreen(self.master, ob)

if __name__=="__main__":
    root = Tk()
    ob = secondscreen(root)
    root.title("MUSIC RECOMMENDATION SYSTEM")
    # make_label(framei, img)
    root.iconbitmap(default="C:/Users/Harshit Soni/Desktop/python/music/icons/music.ico")
    root.configure(background="navy blue")
    root.geometry("320x260")
    root.mainloop()
