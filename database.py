import mysql.connector

def EnterData(name, number):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prudhvi@821",
        database="rasa"
        )
    mycursor=mydb.cursor()

    #mycursor.execute("CREATE TABLE userinformation(name VARCHAR(100),number VARCHAR(100));")
    mycursor.execute("INSERT INTO userinformation(name,number) VALUES ('%s','%s');"%(name,number))

    mydb.commit()
    mydb.close()
