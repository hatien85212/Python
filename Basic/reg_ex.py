import re

#1. Search: Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #find text --> True
y = re.search("\s", txt) #find first white-space character --> 3

if (x):
  print("YES! We have a match!")
else:
  print("No match")

print("The first white-space character is located in position:", y.start())

#2. findall("keyword","string"): Return a list containing every occurrence of "ai":
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
print(len(x))

#3. The split() function returns a list where the string has been split at each match:
#You can control the number of occurrences by specifying the maxsplit parameter:
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
x = re.split("\s", str, 1)
print(x)

#4. The sub() function replaces the matches with the text of your choice:
x = re.sub("\s", "9", str) #Replace every white-space character with the number 9
print(x)
x = re.sub("\s", "9", str, 2)
print(x)

#5. A Match Object is an object containing information about the search and the result.
"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""
str = "The rain in Spain"
x = re.search("ai", str)
print(x.string)
print(x) #this will print an object
x = re.search(r"\bS\w+", str) #looks for any words that starts with an upper case "S":
print(x.span()) #(12,17)
x = re.search(r"\bS\w+", str) #looks for any words that starts with an upper case "S":
print(x.group())

#Metacharacters: Metacharacters are characters with a special meaning https://www.w3schools.com/python/python_regex.asp