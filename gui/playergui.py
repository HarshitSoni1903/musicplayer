from Tkinter import *
import socket
import tkFileDialog
from database import adduser
from Controls import screen2,offlinecontrol,onlinecontrol


class screens:

    #welcome screen check
    def __init__(self,master):
        self.userid = socket.gethostname()
        self.userob = adduser.adduser(self.userid)
        self.userfound = self.userob.atstart()
        if (self.userfound == 0):
            print("not exists")
            self.firstscreen(master)
        elif(self.userfound == 1):
            print("exists")
            print self.userfound
            self.secondscreen(master)
        else:
            print self.userfound

    #if user is not in db
    def firstscreen(self,master):
        self.master = master
        self.framei = Frame(master)
        # framei["bg"] = "light sky blue"
        self.framei.pack()
        self.name = Label(self.framei, text="Please Enter Your Name")
        self.namevar = StringVar()
        self.entry = Entry(self.framei, textvariable=self.namevar)
        self.namevar.set("")
        self.namebutton = Button(self.framei, text="Submit", command = self.addname)
        self.name.grid(row=0, pady=15)
        self.entry.grid(row=1, pady =15)
        self.namebutton.grid(row=2)
        self.entry.bind("<Return>", self.addname)

    #if not then add user
    def addname(self,*args):
        self.username = self.namevar.get()
        self.framei.destroy()
        print("hello "+self.username+" "+self.userid)
        self.userob.insertToUserData(self.userid,self.username)
        self.secondscreen(self.master)

    #if user already in db or has been added
    def secondscreen(self, master):
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
        self.text4.grid(row=3, column=2,columnspan=2, pady=5)
        self.button3.grid(row=4, column=2, columnspan=2)
        self.text5.grid(row=5, column=0, columnspan=4, pady=10)
        self.button1.grid(row=6, column=0, columnspan=4)

    #user chooses to listen to his own choice of music
    def ownmusic(self):
        self.framei.destroy()
        self.offlinescreen(self.master)

    #user chooses to use camera to detect mood
    def camera1(self):
        screen2.camera1(socket.gethostname())
        self.framei.destroy()
        print("added to db")
        self.onlinescreen(self.master)

    """#user chooses to answer questions
    def questions(self):

        self.framei.destroy()
        self.questionscreen(self.master)

    #the question screen
    def questionscreen(self,master):

        self.framei = Frame(master)
        #self.framei["bg"] = "light sky blue"
        self.framei.pack()

        #question1
        self.question1 = Label(self.framei, text="some question<1>")
        self.qla = StringVar()
        self.qla.set("somevalue1")
        self.q1b1 = Radiobutton(self.framei, text = "op1", variable=self.qla, value="somevalue1")
        self.q1b2 = Radiobutton(self.framei, text="op2", variable=self.qla, value="somevalue2")
        self.q1b3 = Radiobutton(self.framei, text="op3", variable=self.qla, value="somevalue3")
        self.q1b4 = Radiobutton(self.framei, text="op4", variable=self.qla, value="somevalue4")
        self.question1.grid(row=0, columnspan=5, pady=10)
        self.q1b1.grid(row=1, column=0, padx=5)
        self.q1b2.grid(row=1, column=1, padx=5)
        self.q1b3.grid(row=1, column=2, padx=5)
        self.q1b4.grid(row=1, column=3, padx=5)

        #question2
        self.question2 = Label(self.framei, text="some question <2>")
        self.q2a = StringVar()
        self.q2a.set("somevalue1")
        self.q2b1 = Radiobutton(self.framei, text="op1", variable=self.q2a, value="somevalue1")
        self.q2b2 = Radiobutton(self.framei, text="op2", variable=self.q2a, value="somevalue2")
        self.q2b3 = Radiobutton(self.framei, text="op3", variable=self.q2a, value="somevalue3")
        self.q2b4 = Radiobutton(self.framei, text="op4", variable=self.q2a, value="somevalue4")
        self.question2.grid(row=2, columnspan=5, pady=10)
        self.q2b1.grid(row=3, column=0, padx=5)
        self.q2b2.grid(row=3, column=1, padx=5)
        self.q2b3.grid(row=3, column=2, padx=5)
        self.q2b4.grid(row=3, column=3, padx=5)

        #question3
        self.question3 = Label(self.framei, text="some question <3>")
        self.q3a = StringVar()
        self.q3a.set("somevalue1")
        self.q3b1 = Radiobutton(self.framei, text="op1", variable=self.q3a, value="somevalue1")
        self.q3b2 = Radiobutton(self.framei, text="op2", variable=self.q3a, value="somevalue2")
        self.q3b3 = Radiobutton(self.framei, text="op3", variable=self.q3a, value="somevalue3")
        self.q3b4 = Radiobutton(self.framei, text="op4", variable=self.q3a, value="somevalue4")
        self.question3.grid(row=4, columnspan=5, pady=10)
        self.q3b1.grid(row=5, column=0, padx=5)
        self.q3b2.grid(row=5, column=1, padx=5)
        self.q3b3.grid(row=5, column=2, padx=5)
        self.q3b4.grid(row=5, column=3, padx=5)"""

    #screen for playing music online

    def onlinescreen(self,master):
        self.framei = Frame(master)
        self.framei["bg"] = "light sky blue"
        self.framei.pack()
        onlinecontrol.getlist()
        print onlinecontrol.index
        self.button1 = Button(self.framei, text="Play", command=onlinecontrol.play)
        self.button2 = Button(self.framei, text="Pause", command=onlinecontrol.pause)
        self.button3 = Button(self.framei, text="Stop", command=onlinecontrol.stop)
        self.button4 = Button(self.framei, text="Resume", command=onlinecontrol.resume)
        self.button5 = Button(self.framei, text="Next", command=onlinecontrol.nextsong)
        self.button6 = Button(self.framei, text="Previous", padx=20, pady=20, command=onlinecontrol.previous)
        #self.button7 = Button(self.framei, text="Browse", command=onlinecontrol.getlist)
        self.button8 = Button(self.framei, text="Shuffle & Play", command=onlinecontrol.shuffleandplay)
        #self.button9 = Button(self.framei, text="Play Selected Song", command=onlinecontrol.playselected)

        global artist,songname, album, genre

        """artist = StringVar()
        songname = StringVar()
        album = StringVar()
        genre = StringVar()"""

        dicti = onlinecontrol.getmeta()
        artist = dicti['artist']
        album = dicti['album']
        genre= dicti['genre']
        songname= dicti['songname']
        self.changevalue()
        self.artistlabel = Label(self.framei,  text = artist)
        self.genrelabel = Label(self.framei,  text = genre)
        self.albumlabel = Label(self.framei,  text = album)
        self.Songnamelabel = Label(self.framei, text = songname)
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
        master.update_idletasks()
    #screen for playing music offline

    def changevalue(self):
        print "inside changevalue"

        """global artist,songname, album, genre
        artist.set(onlinecontrol.artist)
        album.set(onlinecontrol.album)
        genre.set(onlinecontrol.genre)
        songname.set(onlinecontrol.songname)
        print onlinecontrol.artist"""

        self.framei.update()
        root.update_idletasks()

    def offlinescreen(self,master):

        self.framei = Frame(master)
        self.framei["bg"] = "light sky blue"
        self.framei.pack()
        self.button1 = Button(self.framei, text="Play", command=offlinecontrol.play)
        self.button2 = Button(self.framei, text="Pause", command=offlinecontrol.pause)
        self.button3 = Button(self.framei, text="Stop", command=offlinecontrol.stop)
        self.button4 = Button(self.framei, text="Resume", command=offlinecontrol.resume)
        self.button5 = Button(self.framei, text="Next", command=offlinecontrol.nextsong)
        self.button6 = Button(self.framei, text="Previous", padx=20, pady=20, command=offlinecontrol.previous)
        self.button7 = Button(self.framei, text="Browse", command=self.browseandgetlist)
        self.button8 = Button(self.framei, text="Shuffle & Play", command=offlinecontrol.shuffleandplay)
        self.button9 = Button(self.framei, text="Play Selected Song", command=offlinecontrol.playselected)
        self.button1.grid(row=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=0, column=3)
        self.button5.grid(row=0, column=4)
        self.button6.grid(row=0, column=5)
        self.button7.grid(row=2, column=3)
        self.button8.grid(row=2, column=0)
        self.button9.grid(row=2, column=5)

    def browseandgetlist(self):
        self.path = tkFileDialog.askdirectory(title="Select Folder With MP3 Music you Want To Play")
        self.path = self.path+ '/'
        offlinecontrol.getlist(self.path)

    def browseandgetmusic(self):
        self.path = tkFileDialog.askopenfilename(title="Select Mp3 File to be Played")
        offlinecontrol.getlist(self.path)

def doSomething():
    # check if saving
    try:
        offlinecontrol.stop()
    except:
        pass
    try:
        onlinecontrol.stop()
    except:
        pass
    finally:
        root.destroy()

if __name__=='__main__':

    root = Tk()
    musicapp = screens(root)
    root.title("music player")
    root.resizable=False
    root.geometry("640x340")
    root.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
    root.mainloop()

    #print 1