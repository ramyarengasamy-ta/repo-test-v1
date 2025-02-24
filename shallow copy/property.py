class Car:
    def __init__(self, model, speed=0):
        self.model = model
        self._speed = speed  

    @property
    def speed(self): 
        return self._speed

    @speed.setter
    def speed(self, value):  
        if value < 0:
            raise ValueError("Speed cannot be negative!")
        self._speed = value

    def accelerate(self, amount):  
        if amount > 0:
            self._speed += amount
            print(f"The car accelerated! New speed: {self._speed} km/h")
        else:
            print("Acceleration must be positive!")

    def brake(self, amount):  
        if amount > self._speed:
            self._speed = 0  
        else:
            self._speed -= amount
        print(f"The car slowed down. New speed: {self._speed} km/h")


car = Car("Toyota")


print(car.speed)  

car.accelerate(50) 

car.brake(20)  
