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

# Unpack tuples 
# packing - create a tuple and assigning value

fruits = ("apple", "banana", "cherry")

# unpacking 

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
 
# Using Asterisk - *

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits


# Loop through tuple - using for loop 

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# we can also loop thrugh the index number - using range() and len()

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
# using While loop 

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
# tuple can join using the '+' oprator

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# multiply the tuple using '*'

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# tuple methods 

# count() - Returns the number of times a specified value occurs in a tuple

# index() - Searches the tuple for a specified value and returns the position of where it was found