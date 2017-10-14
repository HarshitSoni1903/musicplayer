import dbcon
import mysql.connector

class getmusiclist:
    def __init__(self, tablename):
        self.con=dbcon.Connection()
        self.cnx = self.con.function()
        self.cursorcnx = self.cnx.cursor()
        try:
            self.Table_name = tablename
            self.query = "select * from " + self.Table_name
            print(self.Table_name)
            self.cursorcnx.execute(self.query)
            self.rows = self.cursorcnx.fetchall()
            self.musiclist = []

            for row in self.rows:
                self.musiclist.append(row)

        except mysql.connector.Error as err:
            print(err.msg)
    def getlist(self):
        return self.musiclist

if __name__=="__main__":
    obj=getmusiclist("sadtable")
    obj.getlist()

