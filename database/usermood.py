import mysql.connector
from database import dbcon

class addusermood:

    def __init__(self):
        self.con = dbcon.Connection()
        self.cnx = self.con.function()
        self.cursorcnx = self.cnx.cursor()

    def insertToUserMood(self,userid,period,fear,disgust,anger,neutral,happiness,sad,surprise):
        try:
            self.Table_name = "usermood"
            self.cursorcnx.execute("insert into usermood (userid,period,fear,disgust,anger,neutral,happiness,sad,surprise) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(userid,period,fear,disgust,anger,neutral,happiness,sad,surprise))
            self.cursorcnx._connection.commit()
            return 1
        except mysql.connector.Error as err:
            print err.msg
    def getFromUserMood(self):
        try:
            self.cursorcnx.execute("select userid, period, fear, disgust, anger, neutral, happiness, sad, surprise from usermood")
            self.rows = self.cursorcnx.fetchall()
            self.datalists = []
            for row in self.rows:
                self.datalists.append(row)
            return self.datalists
        except mysql.connector.Error as err:
            print err.msg

    def getUserMood(self,userid,period):
        try:
            self.cursorcnx.execute("select fear, disgust, anger, neutral, happiness, sad, surprise from usermood where userid = %s and period = %s",(userid,period))
            if self.cursorcnx.rowcount<=14:
                self.rows = self.cursorcnx.fetchall()
                #self.user = []
                #print self.rows[-1]
                return 0,self.rows[-1]
            else:
                #for row in self.rows:
                    #print row
                self.rows = self.cursorcnx.fetchall()
                self.user = []
                for row in self.rows:
                    self.user.append(row)
                return 1,self.user

        except mysql.connector.Error as err:
            print err.msg