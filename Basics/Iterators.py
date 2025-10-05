# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

# __iter__() and __next__() Contian this two methods

# Iterator vs Iterable

# Itereable - list , tuple , set and dictionary are the itreable objects they we can itreate throught them

#  iter() - have iter method use to get the itrations

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# even strings are itreable objects

# for loop actually create an iterator object and executes the next() 


# StopIteration to stop the itreation and avoid the infinity exe
