# py -m pip install mysql-connector-python
import mysql.connector
conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password ="W7301@jqir#",
                               database = "sept25pyhton")

sql="select * from studenttt"
cursor = conn.cursor()
cursor.execute(sql)
conn = cursor.fetchall()
print(conn)