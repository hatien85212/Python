#!/usr/bin/python

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print ("Print all keys", tinydict.keys())   # Prints all the keys
print ("Prints all the values: ",tinydict.values()) # Prints all the values
print (tinydict)

#print (tinydict.get("name"))
#tinydict["name"]="Tien" #update
#tinydict["new"]="new" #add new
#tinydict.pop("new") #remove
#tinydict.clear() # empty
