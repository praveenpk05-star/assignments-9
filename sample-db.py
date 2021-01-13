import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "5050"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE sampledb")