import mysql.connector

from database import dbcon

class adduser:

    def __init__(self,userid):
        self.con = dbcon.Connection()
        self.cnx = self.con.function()
        self.cursorcnx = self.cnx.cursor()
        #self.cursorcnx.execute("USE songdb")
        print userid
        self.checkuser = self.checkUserExists(userid)
        print self.checkuser

    def atstart(self):
        return self.checkuser

    def insertToUserData(self, userid,username):
        try:
            print(2)
            self.Table_name = "userdata"
            print(self.Table_name)
            self.cursorcnx.execute("insert into userdata (userid,username) VALUES(%s,%s)",(userid,username,))
            self.cursorcnx._connection.commit()
            self.cursorcnx.close()
            return 1
        except mysql.connector.Error as err:
            print err.msg

    def checkUserExists(self, userid):
        try:
            print(1)
            self.Table_name = "userdata"
            print(self.Table_name)
            self.cursorcnx.execute("select * from userdata where userid = %s",(userid,))
            print("executed")
            self.rows = self.cursorcnx.fetchall()
            if self.cursorcnx.rowcount==0:
                return 0
            else:
                for row in self.rows:
                    print row
                return 1
        except mysql.connector.Error as err:
            print(err.msg)

if __name__=='__main__':
    obj = adduser("TestUser")
    obj.insertToUserData("Testuser","Dummy User")
