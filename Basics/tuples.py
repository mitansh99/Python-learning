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