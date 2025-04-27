import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="ACE")
c=conn.cursor()
c.execute("insert into student values(679,'bharath','Hyderabad',90)")
conn.commit()
c.close()
conn.close()
