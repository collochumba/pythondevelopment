import sqlite3
conn = sqlite3.connect('example1.db')
c = conn.cursor()
#this how you update the contents on the table
c.execute("""UPDATE details SET salary = 600000  WHERE ID = 102""")
c.execute("""UPDATE details SET salary = 700000  WHERE ID = 103""")

c.execute("""SELECT * FROM details""")
for row in c:
    print(row)#prints the details in the table details in a row



