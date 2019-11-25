""" Inculde example of tuple and list
thislist = ["apple", "banana", "cherry"]
thistuple = ("apple", "banana", "cherry")
- initial
- list: 
+ in array []
+ list () construstor: thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
+ sets: {}
+ dictionary: 
- get a particular
- update/replace
- add new item: 
+ thislist.append("orange"); 
+ thislist.insert(1, "orange")
- remove 1 item: 
+ The pop() method removes the specified index, (or the last item if index is not specified):
+ del thislist
+ del thislist[0]
+ thislist.remove["banana"]
+ thislist.discard["banana"]
- Empty the list: a.clear()
- Copy a list: mylist = thislist.copy(); not use list2 = list1 (list2 is reference to list1, change on list1 will apply on list2)
- loop through a list to list down items
- get lenght: len(a)
- Compare item exist in the list: if "abc" in list
"""

""" Tuple
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" # return an error: 'tuple' object does not support item assignment
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

print("Access to the second item: " + thislist[1])

thislist[1] = "blackcurrant" #replace for banana
print("replaced banana by different value: ")
print(thislist)

#- loop through a list
for x in thislist:
  print(x)
  
#- get lenght: len(a)
print(len(thislist))

#- Compare item exist in the list: if "abc" in list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#- add new item: thislist.append("orange"); thislist.insert(1, "orange")
thislist.append("orange")
print(thislist)

print("Insert new item to specific position")
thislist.insert(1, "orange")
print(thislist)

# delete a list
print("pop():")
thislist.pop()
print(thislist)

print("del index 0:")
del thislist[0]
print(thislist)

print("del all")
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) --> NameError: name 'thislist' is not defined

print("empty all")
thislist = ["apple", "banana", "cherry"]
#thislist.clear() #s.clear() (3.3) removes all items from s (same as del s[:])
del thislist[:] #version 2.7
print(thislist)

#- Copy a list: mylist = thislist.copy(); not use list2 = list1 (list2 is reference to list1, change on list1 will apply on list2)
print("copy a list")
thislist = ["apple", "banana", "cherry"]
#mylist = thislist.copy() #version 3.3
mylist = thislist[:]
print(mylist)

# add many items
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#fruits.extend(more_fruits) #extend method is just for list constructor
print("Add many items:", fruits)

#Tuple
print("Unable to change value in a tuple")
thistuple = ("apple", "banana", "cherry")
# thistuple[1] = "blackcurrant" #should return an error 'tuple' object does not support item assignment
# The values will remain the same:
print(thistuple[1])