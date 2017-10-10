import mysql.connector
from database import dbcon

class addusermood:

    def __init__(self):
        self.con = dbcon.Connection()
        self.cnx = self.con.function()
        self.cursorcnx = self.cnx.cursor()

    def insertToUserMood(self,userid,period,fear,disgust,anger,neutral,happiness,sad,surprise):
        try:
            print(2)
            self.Table_name = "usermood"
            print(self.Table_name)
            print (fear)
            print(disgust)
            print(anger)
            print(neutral)
            print(happiness)
            print(sad)
            print(surprise)
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