import pymysql

# Open database connection
db = pymysql.connect("localhost","root","toor","records" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("insert into student values('the rock',69)")
cursor.execute("insert into student values('john wick',58)")
cursor.execute("delete from student where name='john wick'")
cursor.execute("select * from student")
for i in cursor:
    print(i)
print("------------------------")
db.commit()
cursor.execute("delete from student where name='the rock'")
cursor.execute("select * from student")
for i in cursor:
    print(i)
db.commit()
cursor.execute("update student set name='Satyam' where name='Aayush'")
print("------------------------")
cursor.execute("select * from student")
for i in cursor:
    print(i)
print("----------------")
db.rollback()
cursor.execute("select * from student")
for i in cursor:
    print(i)
db.close()
