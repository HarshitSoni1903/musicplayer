from Controls import apiconnect,camera
from database import usermood
import os,sys
from datetime import datetime

def camera1(userid):
    camob = camera.camera()
    camob.capture("temp.jpg")
    r = apiconnect.connectandget("temp.jpg")
    hour = datetime.now()
    period=hour.hour
    print r
    moodob = usermood.addusermood()
    moodob.insertToUserMood(userid, period, r['fear'], r['disgust'], r['anger'], r['neutral'], r['happiness'], r['sadness'], r['surprise'])
    os.remove("temp.jpg")

if __name__=="__main__":
    camera1("Hunt3r")
