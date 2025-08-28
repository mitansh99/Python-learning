# Dictionaries are use to store data in key value pairs == Objects

# ordered*, changeable and do not allow duplicates

# 3.7+ dictionaries are orders

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# dic's items can be reff by key name
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# items have defined orderd that can not be change
# changeable == chnage , add , remove items after dic created

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # not allowed
}
print(thisdict)

# len() to find the length of the dic
print(len(thisdict))

# data type of items can be any data type

# type == <class 'dict'>

print(type(thisdict))

# dict consructor can be use to create dict
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

# assiging items
# can access the value by its key name inside of []

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#also we have get()
x = thisdict.get("modal")

# keys method will return the list of all the keys from dict
x = thisdict.keys()

# add new items to the dicts

thisdict["color"] = "white"

# values this will return all the values from the dict

x = thisdict.values()

# The items() method will return each item in a dictionary, as tuples in a list.

x = thisdict.items()

# check if key exsist
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  

# change the value of spacific item by ref their key name 

thisdict["year"] = 2018

# The update() method will update the dictionary with the items from the given argument.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# adding item into the dict can be done by new index or new key name

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# we can also use update() too for add items to the dict

# pop() can be use to remove the items with key name 
thisdict.pop("model")

#thisdict.popitem() - last insterted item
thisdict.popitem()

# del - key word use to remove item with sapsific key word
del thisdict["model"]

# del keyword without key will del shole dict


# clear() - method clear the dict
thisdict.clear()