import sqlite3
conn = sqlite3.connect('example1.db')
c = conn.cursor()
#this how you view the contents on the table
c.execute("""SELECT * FROM details""")
for row in c:
    print(row)#prints the details in the table details in a row



