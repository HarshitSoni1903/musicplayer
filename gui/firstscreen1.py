from Tkinter import *
import secondscreen
class firstscreen:

    # if user is not in db

    def __init__(self, master):
        self.master = master
        self.framei = Frame(master)
        # framei["bg"] = "light sky blue"
        self.framei.pack()
        self.name = Label(self.framei, text="Please Enter Your Name")
        self.namevar = StringVar()
        self.entry = Entry(self.framei, textvariable=self.namevar)
        self.namevar.set("")
        self.namebutton = Button(self.framei, text="Submit", command=self.addname)
        self.name.grid(row=0, pady=15)
        self.entry.grid(row=1, pady=15)
        self.namebutton.grid(row=2)
        self.entry.bind("<Return>", self.addname)

    #if not then add user
    def addname(self,*args):
        self.username = self.namevar.get()
        self.framei.destroy()
        print("hello "+self.username+" "+self.userid)
        self.userob.insertToUserData(self.userid,self.username)
        ob = secondscreen.secondscreen(self.master)
