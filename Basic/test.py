#!/usr/bin/python

"""Standard Data Types
Numbers
String
List
Tuple: readonly
Dictionary: kind of hash table type
+ They work like associative arrays or hashes found in Perl and consist of key-value pairs
+ key: usually numbers or strings
+ value: can be any arbitrary Python object
+ Dictionaries are enclosed by curly braces ({ })
+ values can be assigned and accessed using square braces ([]): https://www.tutorialspoint.com/python/python_variable_types.htm
"""
#Delete reference: del ...
#Data Type Conversion: https://www.tutorialspoint.com/python/python_variable_types.htm
#Python Bitwise Operators: 
"""Multiple Assignment
a = b = c = 1
a,b,c = 1,2,"john"
"""

#four different numerical types: int, long, float, complex

print ("Hello, Python!")

#Example from https://www.w3schools.com/python/python_syntax.asp

if 5 > 2:
  print("Five is greater than two!") # error if you skip the indentation
  
#2. Docstrings can be one line, or multiline. Python uses triple quotes at the beginning and end of the docstring:

"""This is a 
multiline docstring."""
print("Hello, Docstring!")

#3. Variables: need to be declared with any particular type and can even change type after they have been set
first_name = "Tien" # x is of type int
last_name = "Dao" # x is now of type str
print("Full name: " + first_name + " " + last_name)

#4. Multi-Line Statements

