class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,marks):
        super(Student,self).__init__(name,age)
        self.marks=marks
        print("-----details-----")
        print("Name:"+str(self.name)+"\n" +"age:"+str(self.age)+"\n"+"Marks:"+str(self.marks))
class Company(Student):
    def __init__(self,name,age,marks,salary):
        super(Company,self).__init__(name,age,marks)
        self.salary=salary
        print("-----Multi level inheritance-----")
        print("Name:"+str(self.name)+"\n"+"Age:"+str(self.age)+"\n"+"Marks:"+str(self.marks)+"\n"+"Salary:"+str(self.salary))

#a=Student(input("Enter the name:"),int(input("enter the age:")),int(input("enter the marks:")))

stud = Company("Aayush",22,69,100000000)


