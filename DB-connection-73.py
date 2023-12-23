from mysql.connector import *

try:
    con = connect(host='localhost', user='arif', password='1234', database='myDB')
    mycursor = con.cursor()
    #mycursor.execute("show databases")
    mycursor.execute("select * from student")
    result = mycursor.fetchall()
    for i in result:
        print(i)
except DatabaseError as e:
    print('not able to connect to DB')