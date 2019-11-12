from _thread import start_new_thread as tdd
import time
def func(i):
    fact = 1
    while(i>0):
        fact=fact*i
        i-=1
    print(fact)
tdd(func,(1,))
time.sleep(0.5)
tdd(func,(2,))
time.sleep(0.5)

tdd(func,(3,))
time.sleep(0.5)

tdd(func,(4,))
time.sleep(0.5)

tdd(func,(5,))
time.sleep(0.5)

tdd(func,(6,))
time.sleep(0.5)

tdd(func,(7,))
time.sleep(0.5)

tdd(func,(8,))
time.sleep(0.5)

tdd(func,(9,))
time.sleep(0.5)

tdd(func,(10,))
time.sleep(0.5)

tdd(func,(11,))
time.sleep(0.5)

tdd(func,(12,))
time.sleep(0.5)

tdd(func,(13,))
time.sleep(0.5)

tdd(func,(14,))
time.sleep(0.5)

tdd(func,(15,))

time.sleep(0.5)
tdd(func,(16,))

time.sleep(0.5)
tdd(func,(17,))
input()