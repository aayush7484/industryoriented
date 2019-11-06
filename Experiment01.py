class student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(self.name)
        print(self.marks)
a=list()
n=int(input("Enter total instances: "))
for i in range(n):
    a.append(input("Enter Name: "))
    a.append(input("Enter Marks: "))
for i in range(0,len(a),2):
    a[i]=student(a[i],a[i+1])
    a[i].display()
    a[i]=a[i].name
print(a)

