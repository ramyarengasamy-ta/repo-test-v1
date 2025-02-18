print(len("welcome"))
print(len("apple tree"))

a = input("enter a string")
reversed = ""
 
for item in range(len(a) - 1, -1, -1):
    reversed += a[item]
 
print(reversed)