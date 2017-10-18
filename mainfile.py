from gui import firstscreen,secondscreen,offlinescreen
from Controls import onlinecontrol,offlinecontrol, internetcheck
from Tkinter import *
from socket import gethostname
from database import adduser
from os import _exit

if 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333....:





























































































































































































class screens:

    #welcome screen check
    def __init__(self,master):
        if(internetcheck.is_connected()):
            self.userid = gethostname()
            self.userob = adduser.adduser(self.userid)
            self.userfound = self.userob.atstart()

            if (self.userfound == 0):
                ob = firstscreen.firstscreen(master)

            elif(self.userfound == 1):
                ob = secondscreen.secondscreen(master)
            #else:print self.userfound

        else:
            #print("i came here")
            ob = offlinescreen.offlinescreen()
            #print("object created")
            ob.makescreen(root,ob)

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
        _exit(0)
if __name__=='__main__':

    root = Tk()
    musicapp = screens(root)
    root.title("music player")
    root.geometry("640x340")
    root.protocol('WM_DELETE_WINDOW', doSomething)
    root.mainloop()