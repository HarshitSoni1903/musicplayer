from Tkinter import *
import tktest2

def changevar():
    print "here"
    var.set(tktest2.one)
root=Tk()
var = StringVar()
var.set(tktest2.one)
var.trace('w',changevar)
labelstr = Label(root, textvariable = var)
labelstr.pack()
root.mainloop()