import time 
from threading import Thread
def name():
    name=("ramya")
    print(name)
    time.sleep(5)
def age():
    age=23
    print(age) 
    time.sleep(6) 
thread1=Thread(target=name) 
thread2=Thread(target=age)  
thread1.start()
thread2.start()
thread1.join()
thread2.join()







print("done")