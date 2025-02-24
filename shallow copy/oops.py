class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
print(MathOperations.add(5, 3)) 

class Car:
    brand = "Toyota" 
    @classmethod
    def set_brand(cls, new_brand):
        cls.brand = new_brand
    @classmethod
    def get_brand(cls):
        return cls.brand
print(Car.get_brand())  
Car.set_brand("Honda")
print(Car.get_brand()) 
