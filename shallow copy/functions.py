def greet():
    print("Hello, world!")
greet()  
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  
def add(a, b):
    return a + b

result = add(5, 10)
print(result)  

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()        
greet("Bob")   

def square(num):
    return num * num

result = square(4)
print(result)  

square = lambda x: x * x
print(square(5)) 

add = lambda a, b: a + b
print(add(3, 7))  

square = lambda x: x * x
print(square(5))  



add = lambda a, b: a + b
print(add(3, 7))  

def describe_pet(animal, name="Buddy"):
    print(f"{name} is a {animal}.")

describe_pet("dog")  


describe_pet("cat", "Whiskers")  

def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_to_list("apple"))  
print(add_to_list("banana")) 
def order_pizza(size, crust="thin", toppings="cheese"):
    print(f"Ordered a {size} pizza with {crust} crust and {toppings}.")

order_pizza("large")  


order_pizza("medium", toppings="pepperoni")  


import sys
print("Script Name:", sys.argv[0])  
print("Arguments:", sys.argv[1:])   

import sys

sys.stdout.write("This is standard output.\n")
sys.stderr.write("This is an error message.\n")
