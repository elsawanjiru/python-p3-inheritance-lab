from lib.person.person import Person

class Teacher(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
