import mysql.connector

mydb = mysql.connector.connect("localhost","root","5050","productdb")

mycursor = mydb.cursor()

sql = "SELECT * FROM products WHERE address = 103 "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)