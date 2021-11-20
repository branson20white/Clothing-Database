import sqlite3
from sqlite3 import Error


def create_connection(clothes):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(clothes)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"C:\sqlite\db\clothes.db")
  
# connect sql to the database
connection = sqlite3.connect("database.py")
  
# cursor
crsr = connection.cursor()
  
# print statement will execute if there are no errors
print("Connected to the database")

# SQL command to create a table in the database
sql_command = """CREATE TABLE clothes ( 
id_number INTEGER PRIMARY KEY, 
item_name VARCHAR(20),
color VARCHAR(20), 
fabric VARCHAR(20), 
hood CHAR(3), 
brand VARCHAR(20);"""

# primary key
pk = [1,2, 3, 4, 5, 6]
  
# Enter 5 item names
item_name = ['Atom', 'Ansur', 'Beta', 'Superior Down', 'Event']
  
# Enter 5 colors
color = ['Blue', 'Brown', 'Maroon', 'Brown', 'Green']
  
# Enter 5 fabrics
fabric = ['Down', 'Ripstop', 'Goretex', 'Down', 'Ripstop']
  
# Enter hood variable 
hood = ['No', 'Yes', 'Yes', 'No', 'Yes']

#enter name of brand 
brand = ['Arcteryx', 'Klattermusen', 'Arcteryx', 'Mont Bell', 'And Wander']
  
for i in range(5):
  
    crsr.execute(f'INSERT INTO clothes VALUES ({pk[i]}, "{item_name[i]}", "{color[i]}", "{fabric[i]}", "{hood[i]}", "{brand[i]}")')
  
# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# execute the command to fetch all the data from the table
crsr.execute("SELECT * FROM clothes")
  
# store all the fetched data in the ans variable
ans = crsr.fetchall()
  
for i in ans:
 print(i)

# close the connection
connection.close()