from database import usermood
from datetime import datetime
from socket import gethostname

def checkdb():
    hour = datetime.now()
    period = hour.hour
    userid = gethostname()
    userob = usermood.addusermood()
    check,mooddata = userob.getUserMood(userid,period)
    if check == 0:
        print("entries < 14")
        if (mooddata.index(max(mooddata))!=3):
            return mooddata.index(max(mooddata))
        else:
            mooddata[3]=0
            return mooddata.index(max(mooddata))
    elif check == 1:
        #dosomemath()
        mp = probability(mooddata)
        return mp

def findmood():
    index = checkdb()

    #comment this part later

    #fear,disgust,anger,neutral,happiness,sad,surprise
    if index==0:
        return "feartable"
    elif index==1:
        return "disgusttable"
    elif index==2:
        return "angrytable"
    elif index==3:
        return "neutraltable"
    elif index==4:
        return "happytable"
    elif index==5:
        return "sadtable"
    elif index==6:
        return "surprisetable"
    #return "sadtable"

#checkdb()

def probability(mooddata):
    listi=[]
    for i in mooddata[0]:
        listi.append(0)
    for row in mooddata:
        listi[row.index(max(row))] = listi[row.index(max(row))] + 1

    return listi.index(max(listi))







