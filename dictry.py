user_details = { "name":"ramya","age":"23","place":"chennai"}
print(user_details["name"])
print(user_details["age"])
print(user_details["place"])

dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary["c"])
print("a" in dictionary)
print("b" not in dictionary)


 
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
 
fast_food_items.popitem()
print(fast_food_items)

original_dict = { "name": "Alice", "age": 25 }
copied_dict = original_dict.copy()
original_dict.clear()
print("Copied Dictionary:", copied_dict)
print("Original Dictionary after clearing:", original_dict)
