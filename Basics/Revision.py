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


# Python Set

# Unorderd, unique, mutable - primary use for membership testing and remove duplicates
# creation

setExample = {1, 2, 3}  # literal
setExample = set([1, 2, 2])  # using constructor - result {1,2}

emptySet = set()  # only {} create empty dictionary

emptySet.add(1)  # add item at random place
emptySet.remove(2)  # remove item will give error if item does not exsit
emptySet.discard(20)  # remove - no error


# python dictionaries
#
# data form on key-value pair
# maintain insertion order - update, delete,add

my_dicitonory = {"a": 1, "b": 2}  # - using literal
my_dicitonory = dict(name="mitansh", age="young")  # using constuctor

# empty dictinory can be create by using {} or dict()

# common operations

# access
my_dicitonory["name"]
my_dicitonory.get("name")  # return none when doesn't found

# update
my_dicitonory["age"] = "20"
my_dicitonory.update({"age": "20"})

# delete
del my_dicitonory["name"]
my_dicitonory.pop("name")

# methods
# .keys()
# .values()
# .items()


# enumerate() - use to loop through list
list_data = [0, 1, 2, 3]

for index, value in enumerate(list_data):  # retun index and current value
    print("index is :", index, "and value is", value)

# zip() - flat two list into one

list_1 = [0, 1, 2, 3]
list_2 = [4, 5, 6, 7]

new_list = zip(list_1, list_2)
# new_list = [0,1,2,3,4,5,6,7] zip two list into onew new list

# sorted() vs sort()

a = [1, 7, 9, 2, 4, 5]
sorted(a)  # will return false - check wether list is sorted

a.sort()  # [1,2,4,5,7,9] will sort the list - return sorted new list
