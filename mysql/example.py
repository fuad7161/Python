import mysql.connector
conn = mysql.connector.connect(host='localhost',password='Fuadul11235813',user='root')
if conn.is_istablish():
    print('Connection eshtablished')