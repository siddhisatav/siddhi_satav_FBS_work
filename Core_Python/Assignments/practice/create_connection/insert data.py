# py -m pip install mysql-connector-python
import mysql.connector
conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password ="W7301@jqir#",
                               database = "sept25pyhton")

sql="insert into studenttt(id,fname,lname) values(1,'siddhi' , 'satav')"
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
print(conn)