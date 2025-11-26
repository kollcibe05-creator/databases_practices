import sqlite3

db_connection = sqlite3.connect("./pets_database.db")
db_cursor = db_connection.cursor()

# db_cursor.execute("INSERT INTO cats (name,  breed, age ) VALUES ("Coo-coo", 3, "Majani")")
db_cursor.execute("INSERT INTO cats (name, breed, age) VALUES ('Maru', 'scottish fold', 3)")
