# python does not have built in support for Arrays,

# Have to use NumbPy Lib
# Arrays are used to store mul valuesin in one single var 

cars = ["Ford", "Volvo", "BMW"]

# An array is a special variable, which can hold more than one value at a time.

# Access array elements

x = cars[0]
cars[0] = "TOYOTA"

# len() method use to return length of an array

# -- Looping through the elements
for x in cars:
  print(x)

# Appened() - add item to an array
cars.append("Honda")

# pop() - to remove the element from array
cars.pop(1)

# remove() - to remove the item based on value
cars.remove("Volvo")
