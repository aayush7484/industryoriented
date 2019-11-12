from _thread import start_new_thread
a=1
def factorial(n):
    global a
    a = a * n
    print(a)
    if(n==0 or n==1):
        return 1
    else:
        a = a*n
        return n * factorial(n-1)
start_new_thread(factorial,(3,))