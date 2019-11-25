"""Exceptions: https://www.w3schools.com/python/python_try_except.asp
NameError: occur when a variable is not defined
try...except: handle the error...else: if no errors were raised
try...except...final:  lets you execute code: will be executed regardless if the try block raises an error or not.

"""
import os
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")# run if no error

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") #always to execute regarless errors were raised or not

try:
  f = open("file.txt","r")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()