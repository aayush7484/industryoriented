from threading import Thread
import time

def sleeper(i):
    print("thread %d sleeps for 3 sec "%i)
    time.sleep(3)
    print("thread %d woke up after 3 sec"%i)

for i in range(5):
    t=Thread(target=sleeper,args=(i,))
    t.start()
    time.sleep(0.2)

t.join()
print("Exiting Main Thread")
