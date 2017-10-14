from Tkinter import *

from Controls import onlinecontrol

class onlinescreen:

    def makescreen(self,master,ob):
        self.framei = Frame(master)
        self.framei["bg"] = "light sky blue"
        self.framei.pack()
        onlinecontrol.getlist()
        print onlinecontrol.index
        self.button1 = Button(self.framei, text="Play", command=lambda:onlinecontrol.play(ob))
        self.button2 = Button(self.framei, text="Pause", command=onlinecontrol.pause)
        self.button3 = Button(self.framei, text="Stop", command=onlinecontrol.stop)
        self.button4 = Button(self.framei, text="Resume", command=onlinecontrol.resume)
        self.button5 = Button(self.framei, text="Next", command=onlinecontrol.nextsong)
        self.button6 = Button(self.framei, text="Previous", padx=20, pady=20, command=onlinecontrol.previous)
        #self.button7 = Button(self.framei, text="Browse", command=onlinecontrol.getlist)
        self.button8 = Button(self.framei, text="Shuffle & Play", command=onlinecontrol.shuffleandplay)
        #self.button9 = Button(self.framei, text="Play Selected Song", command=onlinecontrol.playselected)

        global artist,songname, album, genre

        artist = StringVar()
        songname = StringVar()
        album = StringVar()
        genre = StringVar()

        self.listi = onlinecontrol.getmeta()
        indextmp =  onlinecontrol.getindex()
        print(indextmp)
        self.setval(indextmp)

        self.artistlabel = Label(self.framei,  textvar = artist)
        self.genrelabel = Label(self.framei,  textvar = genre)
        self.albumlabel = Label(self.framei,  textvar = album)
        self.Songnamelabel = Label(self.framei, textvar = songname)

        self.button1.grid(row=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=0, column=3)
        self.button5.grid(row=0, column=4)
        self.button6.grid(row=0, column=5)
        #self.button7.grid(row=2, column=3)
        self.button8.grid(row=2, column=0)
        #self.button9.grid(row=2, column=5)
        self.artistlabel.grid(row=3)
        self.genrelabel.grid(row=4)
        self.albumlabel.grid(row=5)
        self.Songnamelabel.grid(row=6)
        #onlinecontrol.index.trace('w',callback=self.changevalue)
        print(1122)
        #print(onlinecontrol.artist)

    def updateval(self,index):
        print "change encountered"
        self.setval(index)

    def setval(self,indextmp):
        global artist, songname, album, genre
        artist.set(self.listi[indextmp][1])
        album.set(self.listi[indextmp][3])
        genre.set(self.listi[indextmp][2])
        songname.set(self.listi[indextmp][0])