import pymysql

# Open database connection
db = pymysql.connect("localhost","root","toor1","records" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
cursor.execute("insert into student values('the rock',69)")
cursor.execute("select * from student")
for i in cursor:
    print(i)

# disconnect from server
db.close()