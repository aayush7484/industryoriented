class Student:


    def __init__(self,counter,age,name):
        self.age = age
        self.name = name
        self.counter=counter +1

    def func(self):
        return str("Name:"+str(self.name)+"\n"+str(self.age)+"\n"+str(self.counter))
    def __del__(self):
        print("Our class is destroyed")
a=Student(int(input("Enter Counter:")),int(input("Enter Age: ")),str(input("Enter Name: ")))
print("---------Output---------")
print(a.func())
#print(a.__del__())
