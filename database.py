import sqlite3
  
# connect sql to the database
connection = sqlite3.connect("database.py")
  
# cursor
crsr = connection.cursor()
  
# print statement will execute if there are no errors
print("Connected to the database")

  
# close the connection
connection.close()