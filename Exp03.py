class Student:
    counter=0

    def __init__(self,age,name):
        self.age = age
        self.name = name

    def func(self):
        return str("Name:"+str(self.name)+"\n"+str(self.age)+"\n"+str(self.counter+1))
    def __del__(self):
        return self.counter
a=Student(int(input("Enter Age: ")),str(input("Enter Name: ")))
print("---------Output---------")
print(a.func())
print(a.__del__())
