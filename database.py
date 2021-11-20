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
hood_or_not CHAR(3), 
brand VARCHAR(20);"""
  
# execute the statement
crsr.execute(sql_command

  
# close the connection
connection.close()