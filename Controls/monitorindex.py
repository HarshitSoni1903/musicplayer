from threading import Thread
import onlinecontrol,offlinecontrol
from gui import onlinescreen,offlinescreen
class monitorthread(Thread):
    def __init__(self):
        Thread.__init__(self)
        #self.threadname=name
    def run(self,master):
        monitor(master)

def monitor(master):
    init = offlinecontrol.getindex()
    while True:
        if(offlinecontrol.getbusy()):
            val = offlinecontrol.getindex()
            if( init== val):
                continue
            else:
                init = val
                offlinescreen.updateval(master,val)
