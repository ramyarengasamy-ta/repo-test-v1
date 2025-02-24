def my_generator():
    yield 2
    yield 3
    yield 4


gen = my_generator()

print(next(gen)) 
print(next(gen)) 
print(next(gen))  
print(next(gen))  


class MyIterator:
    def __init__(self):
        self.num = 1 
    def __iter__(self):
        return self 
    def __next__(self):
        if self.num > 6:  
            raise StopIteration
        value = self.num
        self.num += 1  
        return value


obj = MyIterator()

print(next(obj)) 
print(next(obj))  
print(next(obj))  
print(next(obj)) 