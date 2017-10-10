import dbcon
import mysql.connector


class createlist:
    def __init__(self):
        self.con=dbcon.Connection()
        self.cnx = self.con.function()
        self.cursorcnx = self.cnx.cursor()

        while True:
            choice = int(input("enter 1 for neutral\n2 for sad\n3 for disgust\n4 for anger\n5 for surprise\n6 for fear \n7 for happy \n8 to exit"))
            if(choice==1):
                self.insertToNeurtalTable()
            elif (choice == 2):
                self.insertToSadTable()
            elif (choice == 3):
                self.insertToDisgustTable()
            elif (choice == 4):
                self.insertToAngerTable()
            elif (choice == 5):
                self.insertToSurpriseTable()
            elif (choice == 6):
                self.insertToFearTable()
            elif (choice == 7):
                self.insertToHappyTable()
            elif(choice==8):
                break
            else:
                print("Wrong Code Try Again")

    def insertToHappyTable(self):
        link =  raw_input("enter the link for music")
        songname =  raw_input("enter the Song Name")
        artist =  raw_input("enter artist")
        genre =  raw_input("enter genre")
        album =  raw_input("enter album name")
        try:
            self.Table_name = "happytable"
            print(self.Table_name)
            self.cursorcnx.execute("insert into happytable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s)",(link, songname , artist, genre, album,))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def insertToSadTable(self):
        link =  str(raw_input("enter the link for music"))
        songname = str(raw_input("enter the Song Name"))
        artist =  str(raw_input("enter artist"))
        genre =  str(raw_input("enter genre"))
        album =  str(raw_input("enter album name"))
        try:
            self.Table_name = "sadtable"
            print(self.Table_name)
#            if self.checkTableExists(self.Table_name):
            print "its true"
            self.cursorcnx.execute("insert into sadtable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s)",(link, songname , artist, genre, album,))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def insertToSurpriseTable(self):
        link =  raw_input("enter the link for music")
        songname =  raw_input("enter the Song Name")
        artist =  raw_input("enter artist")
        genre =  raw_input("enter genre")
        album =  raw_input("enter album name")
        try:
            self.Table_name = "surprisetable"
            print(self.Table_name)
            self.cursorcnx.execute("insert into surprisetable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s)",(link, songname , artist, genre, album))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def insertToFearTable(self):
        link =  raw_input("enter the link for music")
        songname =  raw_input("enter the Song Name")
        artist =  raw_input("enter artist")
        genre =  raw_input("enter genre")
        album =  raw_input("enter album name")
        try:
            self.Table_name = "feartable"
            print(self.Table_name)
            self.cursorcnx.execute("insert into feartable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s)",(link, songname , artist, genre, album))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def insertToDisgustTable(self):
        link =  raw_input("enter the link for music")
        songname =  raw_input("enter the Song Name")
        artist =  raw_input("enter artist")
        genre =  raw_input("enter genre")
        album =  raw_input("enter album name")
        try:
            self.Table_name = "disgusttable"
            print(self.Table_name)
            self.cursorcnx.execute("insert into disgusttable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s)",(link, songname , artist, genre, album))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def insertToNeurtalTable(self):
        link =  raw_input("enter the link for music")
        songname =  raw_input("enter the Song Name")
        artist =  raw_input("enter artist")
        genre =  raw_input("enter genre")
        album =  raw_input("enter album name")
        try:
            self.Table_name = "neutraltable"
            print(self.Table_name)
            self.cursorcnx.execute("insert into neutraltable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s,%s)",(link, songname , artist, genre, album))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

    def insertToAngerTable(self):
        link =  raw_input("enter the link for music")
        songname =  raw_input("enter the Song Name")
        artist =  raw_input("enter artist")
        genre =  raw_input("enter genre")
        album =  raw_input("enter album name")
        try:
            self.Table_name = "angrytable"
            print(self.Table_name)
            self.cursorcnx.execute("insert into angrytable(link,Songname,Artist,Genre,Album) VALUES(%s,%s,%s,%s,%s,%s)",(link, songname , artist, genre, album))
            self.cursorcnx._connection.commit()
        except mysql.connector.Error as err:
            print(err.msg)

if __name__=='__main__':
    songob = createlist()