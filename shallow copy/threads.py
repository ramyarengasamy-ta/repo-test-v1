import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")

print_numbers()
print_letters()

print("Both tasks completed!")



import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Number: {i}")

def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")


thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Both tasks completed!")
