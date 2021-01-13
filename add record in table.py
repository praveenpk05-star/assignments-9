import mysql.connector

mydb = mysql.connector.connect("localhost","root","5050","productdb")

mycursor = mydb.cursor()

sql = "INSERT INTO products (id, name, price) VALUES (%d, %s, %d)"
val = (101, "santoor",  30)
mycursor.execute(sql, val)

mydb.commit()
