import sqlite3

conn=sqlite3.connect("test.db")

conn.execute("insert into student values(1,'swasthik');")
conn.execute("insert into student values(2,'swasthik');")
conn.commit()
print("inserted")
conn.execute("update student set name='anchan' where rno=1")
cursor=conn.cursor()
cursor.execute("select * from student")
row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()
cursor.close()
conn.close()
