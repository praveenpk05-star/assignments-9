import mysql.connector

mydb = mysql.connector.connect("localhost","root","5050","productdb")

mycursor = mydb.cursor()

sql = "UPDATE products SET products = 'cinthol' WHERE address = 'dove'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")