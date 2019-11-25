"""
json.load(Json) --> return a object - dictionary
json.dump(Python object: String, dictionary, list,...) --> return a JSON string
Format the Result: 
- indent=4: separator between key and value and between objects
- 
"""
import json
#1. Convert from JSON to Python
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#2. Convert from Python to JSON:
# a Python object (dict):
x = {
  "name": "John",
  "age": 35,
  "city": "New York"
}
# convert into JSON:
print ("convert Python to Json string", x) #a dictionary will covert the data in single quote, JSON is double quote and all are inside of "{" and "}"
y = json.dumps(x) #param is a string like declaration and assignment of a dictionary

# the result is a JSON string:
print(y)

#3. 
print ("Variaty of items to convernt to Json string")
print(json.dumps({"name": "John", "age": 30})) #dictionary: {"key":"value",...} --> Object: {"name": "John", "age": 30}
print(json.dumps(["apple", "bananas"])) #list: ["item1", "item2"] --> Array: ["apple", "bananas"]
print(json.dumps(("apple", "bananas"))) #tuple: ("item1", "item2") --> Array: ["apple", "bananas"]
print(json.dumps("hello")) # a string --> String
print(json.dumps(42)) #int --> number
print(json.dumps(31.76)) #float --> number
print(json.dumps(True)) #True --> boolean: true
print(json.dumps(False)) #False --> boolean: false
print(json.dumps(None)) #None --> null: null

#4. Indent=4(format result) and sort keys
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
#print (json.dumps(x))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print(json.dumps(x, indent=4, sort_keys=True))