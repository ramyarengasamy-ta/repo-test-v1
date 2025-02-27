

def factorial(num):
    returned = 1
    for item in range(num, 1, -1):
        returned *= item
    return returned
print(factorial(10))  
 