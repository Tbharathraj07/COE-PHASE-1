import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="ACE")
c=conn.cursor()

id=input("Enter your id to delete record from DB")

c.execute("delete from student where id=%s",(id,))
conn.commit()
c.close()
conn.close()
