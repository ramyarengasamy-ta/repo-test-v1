person = {
    "name": "ramya",
    "age": 23,
    "city": "thanjavur"
}
print("Keys:", person.keys())
print("Values:", person.values())

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
my_dict = dict(zip(keys, values))
print(my_dict)


user_info = {"name": "John Doe", "age": 30}
user_info.setdefault("email", "Not Provided")
print(user_info)



person = {"name": "Alice", "age": 25}
copied_person = person.copy()
person.clear()
print("Copied Dictionary:", copied_person)  
print("Original Dictionary after clearing:", person)  

