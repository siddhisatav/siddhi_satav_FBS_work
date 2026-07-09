# py -m pip install mysql-connector-python
import mysql.connector
conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               password ="W7301@jqir#")

sql="create database sept25pyhton"
cursor = conn.cursor()
cursor.execute(sql)