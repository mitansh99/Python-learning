# Tuples --------------------

# Tuples are used to store multiple items in a single variable
# A tuple is a collection which is ordered and unchangeable

thistuple = ("apple", "banana", "cherry")

# tuple items ----------------------
# ordered, unchangeable, and allow duplicate values
# items have index and start from 0

# order - items have defined order that will not change

# tuple are unchange able like we can not add - remove items after creation

# tuple allow duplicate values

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# len () ---------------------------------

# to determine how many items tuple have
print(len(thistuple))

# create a tuple with one item ----------------------------
# to create that we have to add comma after one item -  otherwise python does not recognize it as tuple

thistuple = ("apple",)

# tuple items can be any data types - and contain diff datatypes too

tuple1 = ("abc", 34, True, 40, "male")

# type of tuple is - <class 'tuple'>

# tuple constructor 
# possiable to create a tuple using that - tuple()

thistuple = tuple(("apple", "banana", "cherry")) # not double parenthesis 


# tips -----------------**************************************

# *Set items are unchangeable, but you can remove and/or add items whenever you like.

# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered

# Access tuple items -- by the index numbers , insexe square brackets

thistuple = ("apple","banana")
print(thistuple[1]) # first index start from 0

# Nagative Indexing -- start from the last item

thistuple[-1]

# Range of Index -- we can spacify where to start 

# thistuplep[2:5] -- Start with 2nd index and end to 4th index (Not include the last)
print(thistuple[:4]) # Strat from all index

print(thistuple[2:]) # All Items after 2nd index

# same we can do nagitive index

# check item exsist in tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# tuple update -- tuple can not be chnage , add, or remove items once the tuple is created

# Immutables == tuples

# you can convet the value into the list change the value and convert back to the tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# same way to add the value 

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Allow to add tuple into the tuple (concatination)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple

# Note: You cannot remove items in a tuple.

# but we can do the same workaround 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# We can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)