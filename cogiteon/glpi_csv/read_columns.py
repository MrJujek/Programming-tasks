import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
        host="localhost",
        user="glpi",
        password="1qaz2wsx3edcG",
        database="glpi"
)

mycursor = mydb.cursor()
mycursor.execute("show tables;")
result = mycursor.fetchall()

tables = [x[0] for x in result]

for table in tables:
    mycursor.execute(f"select * from {table};")
    rows = mycursor.fetchall()

    if len(rows) < 1:
        continue

    mycursor.execute(f"describe {table};")
    table_data = mycursor.fetchall()
    columns = [x[0] for x in table_data]
    print(columns)