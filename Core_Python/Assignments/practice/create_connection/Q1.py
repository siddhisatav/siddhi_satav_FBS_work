# py -m pip install mysql-connector-python
import mysql.connector
conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password ="W7301@jqir#")

print (conn)