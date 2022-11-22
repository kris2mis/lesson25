# HUMAN, STUDENT, controller - наследование, делегирование

class Human:
    def __init__(self, name, surname, age):
        print("constructor from Human")
        self.name = name
        self.surname = surname
        self.age = age

    def run(self):
        print(f"\nHuman {self.name} is running", end=" ")
