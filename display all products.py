import mysql.connector

mydb = mysql.connector.connect("localhost","root","5050","productdb")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM products")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)