def add_numbers(a:int,b:int):
    return a+b
print(add_numbers(10,20))

def add_numbers(a:int,b:int,v:int):
    return a*b*v
print(add_numbers(1,2,3))

name="ramya"
age=23
place="chennai"

a=f"{name} is {age} old and she lives in{place}"
print(a)

x ="apple"
y="orange"
z="grapes"
fruits=f"{x},{y},{z} are good fruits"
print (fruits)

def rounding(num:float):
    return int(num*100)/100
print(rounding(2345.567))

def rounding(num:float):
    return int(num*100)/100
print(rounding(23.456))

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))  
print(is_prime(10))  

x = [5, 6, 7]
y = x.copy()

y.append(8)

print("List x:", x)  
print("List y:", y)  

print(person["name"])  # "John"
print(person.get("age"))  # 25
print(person.get("job", "Not found"))  # Avoids error if key doesn't exist





