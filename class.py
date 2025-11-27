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