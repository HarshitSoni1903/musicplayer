import onlinecontrol
from gui import playergui

global artist,songname, album,genre

class meta(object):
    def get_value(self):
        self.artist=playergui.artist
        self.songname=playergui.songname
        self.album=playergui.album
        self.genre=playergui.genre

    def set_value(self):

        onlinecontrol.root.update()