class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):  
        return f"{self.name} - ${self.price}"
class ShoppingCart:
    def __init__(self):
        self.items = []  

    def __add__(self, product):  
        if isinstance(product, Product): 
            self.items.append(product)
        return self  
    def __len__(self):  
        return len(self.items)

    def __str__(self):  
        cart_items = "\n".join(str(item) for item in self.items)
        total_price = sum(item.price for item in self.items)
        return f"Shopping Cart:\n{cart_items}\nTotal: ${total_price}"

p1 = Product("Laptop", 1000)
p2 = Product("Headphones", 200)
p3 = Product("Mouse", 50)


cart = ShoppingCart()


cart = cart + p1
cart = cart + p2 + p3  


print(cart)  
print(f"Total items: {len(cart)}")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self): 
        return f"{self.name} - ${self.price}"


class ShoppingCart:
    def __init__(self):
        self.items = [] 

    def __add__(self, product): 
        self.items.append(product)
        return self  

    def __len__(self): 
        return len(self.items)

    def __str__(self): 
        cart_items = "\n".join(str(item) for item in self.items)
        total_price = sum(item.price for item in self.items)
        return f"Shopping Cart:\n{cart_items}\nTotal: ${total_price}"



p1 = Product("Laptop", 1000)
p2 = Product("Mouse", 50)

cart = ShoppingCart()

cart = cart + p1 + p2 


print(cart)
print(f"Total items in cart: {len(cart)}")




class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):  
    pass

print(D.mro())  
