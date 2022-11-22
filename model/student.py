# HUMAN, STUDENT, controller - наследование, делегирование

from model.human import Human


class Student(Human):
    # переопредление метода - этот конструктор перекроет конструктор Human

    def __init__(self, name, surname, age, mark=4):
        print("constructor from Student class")
        # self.name = name  - это copy past  - вместо этого используем функцию
        # self.surname = surname
        # self.age = age
        super().__init__(name, surname, age)  # - это ДЕЛЕГИРОВАНИЕ

        self.mark = mark

    def run(self):
        # print(f"Student {self.name} is running to canteen")
        super().run()
        print(f"to canteen")

    def study(self):
        self.run()  # это важное качество использования метода класса в другом методе другого класса
        print(f"Student {self.name} is studying.")

# s1 = Student("Alex")
# print(s1.name)
# s1.run()
# s1.study()  # расширение по методу

# s2 = Student("Kate")
# print(s2.name)
# s2.run()
# s2.study()
