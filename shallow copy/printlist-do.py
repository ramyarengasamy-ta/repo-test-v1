def print_list_info(lst):
   
    print(f"List: {lst}")
    print(f"Length: {len(lst)}")
    print(f"Type of elements: {set(type(item) for item in lst)}")
    print(f"Memory Address: {hex(id(lst))}")
    
    if not lst:
        print("The list is empty.")
    else:
        print("The list is not empty.")
    
    duplicates = set([x for x in lst if lst.count(x) > 1])
    if duplicates:
        print(f"Duplicates: {duplicates}")
    else:
        print("No duplicates found.")


my_list = [1, 2, 3, 2, "hello", "hello", 3.14]
print_list_info(my_list)
