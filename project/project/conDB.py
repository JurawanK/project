import mysql.connector


def conDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="project",
        password="1234",
        database="project",
    )
    return mydb


class Con:
    def addHW(name, hw_name):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO test (name, hw_name, status, value) VALUES ('{}', '{}','OPEN',0.00)".format(name, hw_name)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        ID = mycursor.lastrowid
        return ID
    
    def DeleteHW(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM test WHERE id = {}".format(ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def getHWByID(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT status,value,auto FROM test WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def updateStatusHW(ID, status):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE test SET status = '{}' WHERE id = {}".format(status, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def updateValueHW(ID, value):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE test SET value = {} WHERE id = {}".format(value, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def getAllHW():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM test"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def getValueHWByID(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT VALUE FROM test WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def getStatusHWByID(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT STATUS FROM test WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def updateStatusValueHW(ID, status, value):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE test SET status = '{}', value = {} WHERE id = {}".format(status, value, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def getAutoHWByID(ID):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT AUTO FROM test WHERE id = {}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def updateAutoHW(ID, auto):
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE test SET auto = '{}' WHERE id = {}".format(auto, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True