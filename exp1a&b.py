class student:
    codename="John Wick"
    id=18728

    def __init__(self,a):
        self.a=a


    def add(self):
        n=int(input())
        for i in range(n):
            name=input()
            marks=int(input())
            a.append(name)
            a.append(marks)
        print(a)
a=list()
s=student(a)
s.add()
print(getattr(s,"codename",27))
print(hasattr(s,'codename'))
setattr(s,'codename','Jonathan Wick')
print(s.codename)
delattr(student,'id')
print(hasattr(s,'id'))
