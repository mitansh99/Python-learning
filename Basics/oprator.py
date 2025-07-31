# Operators are use to perform opration on the values or the variables

# Type of oprators ------------------------
x=y= 5 

# Arithmetic operators -------------------
x + y # Addition
x - y # Subtraction 
x * y # Multipication
x / y # Division 
x % y # Modulus
x ** y # Exponentiation
x // y # Floor division

# Assignment operators -----------------------------
x = y
x += y
x -= y
x *= y
x /= y
x %= y
x //= y
x **= y
x &= y
x |= y
x ^= y
x >>= y
x <<= y
print(x:=3)  # 	x = 3 print(x)

# Comparison operators --------------------

x == y # Equal
x != y # not Equal
x > y # Less then 
x >= y # Greater then or equal
x <= y # Less then or Equal

# Logical operators ------------------------

x and y # retun true if both statment are true
x or y # return true if any of one is true
not(x) # reverse the result 

# Identity operators

x is y # True if both var are same object
x is not y # True if both var are not same obj
 
# Membership operators ------------------------------------

x in y # True if the sequence with the spacific value is present in obj
x not in y # viceversa

# Bitwise operators ----------------------------------

x & y # set each bit to 1 if both bits are 1
x | y # set each bit to 1 if one of both bit is 1
x ^ y # set each bit to one if only one of two bitd is 1
~x # Inverts all the bits
x << 2 # left shift
x >> 2 # right shift

# Operator precedence

# desc.. the Order in which operations are performed.

print((6 + 3) - (6 + 3)) # higest precedence is ()

print(100 + 5 * 3) # multiplication * have higer precedence then Addition +

