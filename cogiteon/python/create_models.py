import mysql.connector
print("asd")
mydb = mysql.connector.connect(
        host="192.168.22.36",
        user="glpi",
        password="1qaz2wsx3edcG",
        database="glpi"
)

print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM `glpi_plugin_datainjection_mappings`")
myresult = mycursor.fetchall()
for x in myresult:
        print(len(x))
        print(x)