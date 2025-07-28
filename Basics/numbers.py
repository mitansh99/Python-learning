
# Numbers in Python ------------------------------------

# 1. Int 
# -> Any positive and nagative number, whole number, without dcimals or unlimited length
x = 1
y = 35656222554887711
z = -3255522

# 2. Float
# -> positive or natigative number who contains 1 or more decimals.
x = 1.10
z = -35.59
# -> Float can also be scientific numbers with an "e" indicate the powe of 10.
x = 35e3
y = 12E4
z = -87.7e100

# 3. Complex
# -> complex number is writern with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

# Type conversion can be done by the functions : int(), float(), complex()
x = 10   # int
y = 3.14  # float
z = 5j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

# 4. Random Number 
# -> Python do not have random() to make random number 
# -> it has built in module random that create random numbers
import random

print(random.randrange(1,10))


#! Casting in python is done using the CONSTUCTOR functions:

# ->int() - constructs an integer number from an integer literal
#           a float literal (by removing all decimals)
#           a string literal (providing the string represents a whole number)

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# float() - constructs a float number from an integer literal, 
#           a float literal
#           a string literal (providing the string represents a float or an integer)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'