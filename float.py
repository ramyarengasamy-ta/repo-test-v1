x = 10.5
print(isinstance(x, float)) 

print(float(5))      
print(float("3.14")) 
print(float("inf"))  
print(float("nan"))  

print(0.1 + 0.2) 
print(round(0.1+0.2,2))


from decimal import Decimal
x = Decimal("0.1") + Decimal("0.2")
print(x) 

num = 3.14159
print(f"{num:.2f}") 
print(f"{num:.5f}")  
print(f"{num:.3f}")

