
from abc import ABC, abstractmethod

class Restaurant(ABC): 
    @abstractmethod
    def serve_food(self):
        pass 

class PizzaHut(Restaurant):  
    def serve_food(self):
        return "Serving Pizza "

class KFC(Restaurant):  
    def serve_food(self):
        return "Serving Fried Chicken"
p = PizzaHut()
print(p.serve_food())  

k = KFC()
print(k.serve_food())  

