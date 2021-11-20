import sqlite3
  
# connect sql to the database
connection = sqlite3.connect("database.py")
  
# cursor
crsr = connection.cursor()
  
# print statement will execute if there are no errors
print("Connected to the database")

# SQL command to create a table in the database
sql_command = """CREATE TABLE clothes ( 
item_name INTEGER PRIMARY KEY, 
color VARCHAR(20), 
fabric VARCHAR(20), 
hood CHAR(3), 
brand VARCHAR(20);"""

# execute the statement
crsr.execute(sql_command

# primary key
pk = [2, 3, 4, 5, 6]
  
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
  
    # This is the q-mark style:
    crsr.execute(f'INSERT INTO emp VALUES ({pk[i]}, "{item_name[i]}", "{color[i]}", "{fabric[i]}", "{hood[i]}", "{brand[i]}")')
  
# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()


  
# close the connection
connection.close()