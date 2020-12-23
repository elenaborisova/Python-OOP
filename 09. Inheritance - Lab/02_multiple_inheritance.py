class Person:
    @staticmethod
    def sleep():
        return "sleeping..."


class Employee:
    @staticmethod
    def get_fired():
        return "fired..."


class Teacher(Person, Employee):
    @staticmethod
    def teach():
        return "teaching..."


p = Person()
e = Employee()
t = Teacher()

print(p.sleep())
print(e.get_fired())

print(t.sleep())
print(t.get_fired())
print(t.teach())