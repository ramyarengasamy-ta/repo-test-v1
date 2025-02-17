celsius = int(input("Please enter an integer value for degrees celsius. "))
def fahrenheit(cel):
     return round((1.8 * cel + 32), 1)
 
 
print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")