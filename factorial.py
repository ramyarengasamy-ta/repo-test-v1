
def factorial(num):
    
    returned = 1
    
    for item in range(num, 1, -1):
        returned *= item
 
    
    return returned
 
 
print(factorial(8))  
print(factorial(5))  
print(factorial(6))  