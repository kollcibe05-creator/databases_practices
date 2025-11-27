import sqlite3

db_connection = sqlite3.connect("./pets_database.db")
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE IF NOT EXISTS tester(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age INTEGER)")
class Cat:
    all = []
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.add_cat_to_all(self)
    @classmethod
    def add_cat_to_all(cls, cat):
        cls.all.append(cat)

    def save(self, cursor):
        cursor.execute(
            'INSERT INTO tester (name, breed, age) VALUES (?,?,?)',
            (self.name, self.breed, self.age)

        )    
# # db_cursor.execute("INSERT INTO cats (name,  breed, age ) VALUES ("Coo-coo", 3, "Majani")")
# db_cursor.execute("INSERT INTO cats (name, breed, age) VALUES ('Maru', 'scottish fold', 3)")

# db_cursor.execute("CREATE TABLE IF NOT EXISTS workers (id INTEGER PRIMARY KEY, name TEXT)")
Cat("chiwawa", "doggy", 6)
Cat("chiwoo", "doggy", 5)






for cat in Cat.all:
    cat.save(db_cursor)

db_connection.commit()

for row in db_cursor.execute("SELECT * FROM tester"):
    print(row)

print("----------------------------------------------")    

db_cursor.close()

print("\nDatabse operations completed. Data saved to tester in pets_database.db ")





