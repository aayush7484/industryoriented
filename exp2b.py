class Person:
    def __init__(self,name):
        self.name=name
    def display(self):
        return print(self.name)


class Student(Person):
    def display(self):
        name=input()
        return name
a=Student("Adonis")
print(a.display())