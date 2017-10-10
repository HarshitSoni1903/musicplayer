from database import dbcon
import mysql.connector
con = dbcon.Connection()
cnx = con.function()
print("connected")
cursorcnx=cnx.cursor()

def insertToUserData( userid, username):
    try:
        Table_name = 'userdata'
        print(Table_name)
        insert=(
            "insert into userdata (userid,username) VALUES(%s,%s)"
        )
        arg=(userid,username)
        cursorcnx.execute(insert,arg)
        cursorcnx._connection.commit()
        print("executed")

    except mysql.connector.Error as err:
        print err.msg

def checkData(userid):
    try:
        Table="userdata"
        cursorcnx.execute("select * from userdata WHERE userid = %s ",(userid,))
        rows = cursorcnx.fetchone()
        print rows
        #print(cursorcnx.rowcount)
        #for row in rows:
           #print row
    except mysql.connector.Error as err:
        print err.msg

checkData("harshit")
#insertToUserData("testuser","testuser")
print "after"
checkData("testuser")