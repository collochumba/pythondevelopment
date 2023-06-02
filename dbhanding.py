import sqlite3
conn = sqlite3.connect('example1.db')
c = conn.cursor()
#how to create the table in the database
#use excute
c.execute("""CREATE TABLE IF NOT EXISTS details(id INT PRIMARY KEY, name TEXT,salary REAL)  """)
#INSERTING VALUES TO THE TABLE
c.execute("INSERT INTO details(id,name,salary) VALUES(101,'COLLINS',1000000)")
c.execute("INSERT INTO details(id,name,salary) VALUES(102,'EBBY',1000000)")
c.execute("INSERT INTO details(id,name,salary) VALUES(103,'COBIE',1000000)")
conn.execute("COMMIT")#COMMIT the data to the database



