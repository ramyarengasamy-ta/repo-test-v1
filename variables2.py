import random
random.seed(42)

def print_memory_address(var):
    print(hex(id(var)))

my_value2=12
print_memory_address(my_value2)    

my_value2=10
print_memory_address(my_value2)  

my_int1=42
my_int2=42
my_int3=42
print_memory_address(my_int1)
print_memory_address(my_int2)
print_memory_address(my_int3)

my_bool1=True
my_bool2=True
my_bool3=False
print_memory_address(my_bool1)
print_memory_address(my_bool2)

my_float=42.0
print_memory_address(my_float)

my_none1=None
print_memory_address(my_none1)
my_list1=[1,2,3]
my_list2=my_list1
print_memory_address(my_list1)
print_memory_address(my_list2)
my_list1[0]=-1
print(my_list1)
print(my_list2)