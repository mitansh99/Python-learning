# Lists
# Indexing, slicing
# methods: append(), pop(), sort(), reverse()
# List comprehension
#
# list -- array
# built in, changable, collection of items, support mix datatype

listDef = [0, 1, 2, 3, 4, 5, 6]

# actions
listDef.append(7)  # append single item at the end of the list
listDef.insert(6, 10)  # add element at given index
listDef.remove(2)  # will remove the frst appreing value '2'
a = listDef.pop(3)  # remove the item and retun that - from given index
listDef.clear()  # remove all elements from the list make it empty
listDef.sort()  # sort list-modify orignal
listDef.reverse()  # reverse the list element

# Strings
# Slicing
# methods: split(), join()
# Immutability concept

# string can be define by using '...', "...", """...""" or '''...'''

# imutable - after creation can't be modify oprations create a new string

str = "Mitansh"

a = str[0]  # indexing - getting char by index no
a = str[0:3]  # slicing - will retutn 1 to 3 index char
a = str[0:3:-1]  # revive the sliced string
str[::-1]  # return the reversed string

# nagaive index allow you to count backwords
# if slice went out of the range then retun max possible ans
# can use slice() constructor for programmatically slicing

# operations
# + - for concatination
# * - for mltiplying
# in - check membership
# not in - "


# common string method
len(str)  # - length of str
str.upper()  # - covert sting into upper - same for lower()
