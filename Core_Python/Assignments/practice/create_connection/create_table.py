# py -m pip install mysql-connector-python
import mysql.connector
conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password ="W7301@jqir#",
                               database = "sept25pyhton")

sql="create table studenttt(id int , fname varchar(20),lname varchar(20))"
sql="table studenttt"
cursor = conn.cursor()
cursor.execute(sql)

print(conn)