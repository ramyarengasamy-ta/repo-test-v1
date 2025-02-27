import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  
        print(f"Execution time: {time.time() - start:.3f} seconds") 
        return result
    return wrapper

@time_it 
def calsum(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    print(total)
    return total
calsum(10, 20, 30, a=2, b=4)
