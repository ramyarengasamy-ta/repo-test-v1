my_dict1={'a':1,'b':2}
my_dict2={'a':3,'d':4}
my_dict3={'e':5,'f':6}

my_result_dict1={**my_dict1,**my_dict2}
print(my_result_dict1)

def print_string_info(string):
    print(f"String: {string}, Length: {len(string)}, Memory: {hex(id(string))}")

my_name = "ramya"
print_string_info(my_name)

