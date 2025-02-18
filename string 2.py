s="there are no capitals here"
print(s.upper())
a="THERE ARE NO CAPITALS HERE"
print(a.lower())
print("all caps".isupper())
mixedcase = "A Song of Ice and Fire"
print(mixedcase.isupper())  
print(mixedcase.islower())  
print(mixedcase.upper())  
print(mixedcase.lower())  
print(mixedcase.istitle())  
title_case = mixedcase.title()
print(title_case)  
print(mixedcase.startswith("A"))  
print(mixedcase.endswith("e"))  
words = mixedcase.split()
print(words)  
print("".join(words).isalpha())