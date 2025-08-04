# List ----------------------
# list are use to store multipule value in a single variable

# Built in datatypes

thislist = ["apple" , "banana", "cherry"]
print(thislist)

# List items are orderd, changable, and allow duplicate val

# items have indeies , access bu the [0] second [1]  ---> define order that will not gona change

# list is mutable , add , change , remove items after creating list
# allow duplicate because diff by indesies

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# len() to get the number of the items list contains

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# List can contain diffrent types of values

# list type is a <class 'list'>
print(type(thislist))

# we can use list constructor to create a new list

thislist = list(("apple", "banana", "cherry")) 

# Access List items  ----------------------------------------

print(thislist[1]) # First item have 0 index

# Nagative indexing means start from the back 
# -1 for the last element and so on 

# Range of indexies -------------------------

thislist[2:5] # always return new list 

# srearch will be 2 (inc) bto 5(not inc)

# [:4] for start from first and end to the 4 th element
# [2:] start from 2 and all availabale elemetns

if "apple" in thislist:  # To find iteam avaiable or not
    print("yes it is") 

# Change Item value

thislist[1] = "guwawa" # replace the value with new 

# Range of value change  
thislist[1:3] = ["blackbarry","watermalon"]

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly


# The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist[1:3] = ["watermelon"]

# Insert() use to add the new value to the list whitout replacing exe values

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # insert(index, value)





