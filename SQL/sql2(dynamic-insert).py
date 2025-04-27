import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="ACE")
c=conn.cursor()

id=input("Enter id")
name=input("Enter name")
city=input("Enter city")
marks=input("Enter marks")


c.execute("insert into student values(%s,%s,%s,%s)",(id,name,city,marks))
conn.commit()
c.close()
conn.close()
