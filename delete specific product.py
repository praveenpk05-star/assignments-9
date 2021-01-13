import mysql.connector

mydb = mysql.connector.connect("localhost","root","5050","productdb")

mycursor = mydb.cursor()

sql = "DELETE FROM products WHERE address = 'dettol' "

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")