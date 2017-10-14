import mysql.connector

from mysql.connector import errorcode

class Connection:
    def function(self):
        self.cnx=None
        try:
            self.cnx = mysql.connector.connect(user='root', password='ABCD',host='127.0.0.1',database='SongDB')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return None
            else:
                print(err)
        return self.cnx
