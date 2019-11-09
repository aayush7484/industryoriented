def myfunc():
    """'myfunc' documentation.
    SATYAM IS CHUT"""
    pass
print( myfunc.__doc__)

class func:
    temp=1
print(func.__dict__)

def func():
    pass
func.a=1
print(func.__dict__)