# stets are used to store multipule values in single var

# sets = unordered, unchangeable*, and unindexed
thisset = {"apple", "banana", "cherry"}

# Sets are unordered, so you cannot be sure in which order the items will appear.

# Sets - do not allow duplicate values.

# We can't remove the items from the set but we can remove items

# true and 1 is equal in sets (SAME VALUE) FALSE == 0

len(thisset) # get the length of the set

type(thisset) # <class 'set'>

# It is also possible to use the set() constructor to make a set.


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

# We can not access the items of the set by index or th key
# only way is to loop through it

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
print("banana" in thisset) 

# After creation of the set we can not change the items of the set but we can add new items to the set

# items in set can be added by using add() 

thisset.add("pinapple")

# update() -  To add items from the another set to the current set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# the object in the update() does not have to be set - it can be any itrable items
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

# remove() / discard() -- to remove items from the set

thisset.remove("banana")


# If the item to remove does not exist, remove() will raise an error.

thisset.discard("banana")

# discard() will NOT raise an error.

# pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.\
    
thisset.clear() # clear the set


del thisset # use to delete the set completly
