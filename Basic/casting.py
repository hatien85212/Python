""" times when you want to specify a type on to a variable
Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
w = float("3")   # z will be 3.0
t = str(w)
print(x)
print(y)
print(z)
print(w)
print("Str: " + t)