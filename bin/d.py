#mysql
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    password='Fuadul11235813',
    user='root',
    database = 'db1'
    )
cur = conn.cursor()

s = 'select * from book'
cur.execute(s)
result = cur.fetchall()
for i in result:
    print(i)

#insert multiple data
# s = 'insert into book(bookid,title) values(%s,%s)'
# books = [(2,'masud'),(3,'imran'),(4,'bishow')]
# cur.executemany(s,books)
# conn.commit()

#insert data in table..
# s = 'insert into book (bookid , title) values(%s,%s)'
# a = [1,'hallet plakard']
# cur.execute(s,a)
# conn.commit()

# create table.. in the mentioned database
# s = 'create table book(bookid integer(4),title varchar(20))'
# cur.execute(s)

#create database
#cur.execute("CREATE DATABASE db1")




# for i in range(1,10,2):
#     print(i)

# name = 'fuad'
# print('Name: '+name)
# radius = int(input())
# area = radius*3.14
# print("Area: {}".format(area))
# print("Area: "+str(area))

# comparison operator
# x = 5==5
# print(x)

#case conversion
# s = ' My name is Fuadul.My home in Rajbari '
# tem = s.strip()
# a = tem.replace('My','MoyMoy')
# print(a)
# print(s.lower())
# print(s.upper())
#print(tem.replace('M' , 'F'))
# print(s.find('M'))

# # take two number and print the sum
# a = float(input())
# b = float(input())
# print(a+b)


# # datatype
# year = input('give your birthday year: ')
# year = int(year)
# print(1920 - year)


# print
# name = input("type your name: ")
# print("Hi "+name)
# print('HI {}'.format(name))
# print(f'HI {name}')
